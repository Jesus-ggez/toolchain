use proc_macro::TokenStream;
use quote::{format_ident, quote};
use syn::{parse_macro_input, Field, Fields, ItemStruct, Type, TypeTuple};

#[proc_macro]
pub fn define_model(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as ItemStruct);
    let struct_name = &input.ident;

    let diesel_struct_name = format_ident!("{}Db", struct_name);
    let py_struct_name = format_ident!("{}Py", struct_name);

    let mut rust_fields = vec![];
    let mut diesel_fields = vec![];
    let mut field_names = vec![];

    if let Fields::Named(fields_named) = &input.fields {
        for field in &fields_named.named {
            let name = field.ident.clone().unwrap();
            field_names.push(quote! { #name });

            match &field.ty {
                Type::Tuple(TypeTuple { elems, .. }) if elems.len() == 2 => {
                    let rust_ty = &elems[0];
                    let diesel_ty = &elems[1];

                    rust_fields.push(quote! { pub #name: #rust_ty });
                    diesel_fields.push(quote! { pub #name: #diesel_ty });
                }
                ty => {
                    rust_fields.push(quote! { pub #name: #ty });
                    diesel_fields.push(quote! { pub #name: #ty });
                }
            }
        }
    } else {
        panic!("Solo se admiten structs con campos nombrados");
    }

    let main_struct = quote! {
        #[derive(serde::Serialize, serde::Deserialize, Debug, Clone)]
        pub struct #struct_name {
            #(#rust_fields,)*
        }
    };

    let diesel_struct = quote! {
        #[derive(diesel::Queryable)]
        pub struct #diesel_struct_name {
            #(#diesel_fields,)*
        }
    };

    let py_struct = quote! {
        #[derive(pyo3::FromPyObject, pyo3::IntoPyObject, Debug)]
        pub struct #py_struct_name {
            #(#rust_fields,)*
        }
    };

    let from_diesel = quote! {
        impl From<#diesel_struct_name> for #struct_name {
            fn from(db_model: #diesel_struct_name) -> Self {
                Self {
                    #(
                        #field_names: db_model.#field_names,
                    )*
                }
            }
        }
    };

    let from_py = quote! {
        impl From<#struct_name> for #py_struct_name {
            fn from(model: #struct_name) -> Self {
                Self {
                    #(
                        #field_names: model.#field_names,
                    )*
                }
            }
        }
    };

    quote! {
        #main_struct
        #diesel_struct
        #py_struct
        #from_diesel
        #from_py
    }
    .into()
}
