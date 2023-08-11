from abc import ABC, abstractmethod


class BaseStorage(ABC):

    '''统一记忆存储抽象类,基于当前抽象类扩展其他的存储模块'''

    @abstractmethod
    def search(self, query_text: str, owner: str) -> list[str]:
        '''检索记忆,只返回关联性最强的记忆'''
        pass

    @abstractmethod
    def save(self, query_text: str, owner: str) -> None:
        '''保存记忆'''
        pass

    @abstractmethod
    def clear(self, owner: str) -> None:
        '''清空记忆'''
        pass