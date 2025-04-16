use proc_macro::TokenStream;
use quote::{format_ident, quote};
use syn::{parse_macro_input, Field, Fields, ItemStruct, Type, TypeTuple};

#[proc_macro]
pub fn define_model(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as ItemStruct);
    let struct_name = &input.ident;
    let diesel_struct_name = format_ident!("{}Db", struct_name);
    let py_struct_name = format_ident!("{}Py", struct_name);

    let fields = if let Fields::Named(fields_named) = &input.fields {
        fields_named
            .named
            .iter()
            .map(|field| {
                let name = &field.ident.as_ref().unwrap();
                let (rust_ty, diesel_ty) = match &field.ty {
                    Type::Tuple(TypeTuple { elems, .. }) if elems.len() == 2 => {
                        (&elems[0], &elems[1])
                    }
                    ty => (ty, ty),
                };
                (name, rust_ty, diesel_ty)
            })
            .collect::<Vec<_>>()
    } else {
        panic!("Solo se admiten structs con campos nombrados");
    };

    let generate_struct = |name, use_rust_ty: bool| {
        let fields = fields.iter().map(|(name, rust_ty, diesel_ty)| {
            let ty = if use_rust_ty { rust_ty } else { diesel_ty };
            quote! { pub #name: #ty }
        });
        quote! { #(#fields,)* }
    };

    let main_struct = quote! {
        #[derive(serde::Serialize, serde::Deserialize, Debug, Clone)]
        pub struct #struct_name { #generate_struct(struct_name, true) }
    };

    let diesel_struct = quote! {
        #[derive(diesel::Queryable)]
        pub struct #diesel_struct_name { #generate_struct(diesel_struct_name, false) }
    };

    let py_struct = quote! {
        #[derive(pyo3::FromPyObject, pyo3::IntoPyObject, Debug)]
        pub struct #py_struct_name { #generate_struct(py_struct_name, true) }
    };

    let impl_conversion = |from, to, fields| {
        let conversions = fields
            .iter()
            .map(|(name, _, _)| quote! { #name: from.#name });
        quote! {
            impl From<#from> for #to {
                fn from(from: #from) -> Self { Self { #(#conversions,)* } }
            }
        }
    };

    quote! {
        #main_struct
        #diesel_struct
        #py_struct
        #impl_conversion(#diesel_struct_name, #struct_name, fields)
        #impl_conversion(#struct_name, #py_struct_name, fields)
    }
    .into()
}
