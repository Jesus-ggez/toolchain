from abc import ABC, abstractmethod


class Tree(ABC):
    @abstractmethod
    def pre_process(self) -> None:
        ...


    @abstractmethod
    def tokenize(self) -> None:
        ...


    @abstractmethod
    def to_tasm(self) -> None:
        ...


    @abstractmethod
    def executor(self) -> None:
        ...
