from typing import Protocol, TypedDict, Callable, Any
from functools import wraps
from main.utils.constants import hooks
from main.factories.city.preprocessing_city import CheckingCityPreprocessingFactory


class ProcessorProtocol(Protocol):
    """Define um protocolo para implementações que usam o decorador de pré-processamento."""

    def preprocessing(self, obj: Any) -> None:
        """Executa o pré-processamento antes do método original."""
        ...


def preprocessing(processor: type[ProcessorProtocol]) -> Callable[..., Any]:
    """Decorador que aciona o pré-processamento antes da chamada do método."""

    def decorate(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(self, *args, **kwargs) -> Any:
            processor().preprocessing(self)
            return func(self, *args, **kwargs)

        return wrapper

    return decorate


class CityTracker(TypedDict):
    origin: int
    # Outros campos do dataclass


class CheckingAccountPreprocessing(ProcessorProtocol):
    """Realiza o pré-processamento sobre a cidade antes do fluxo principal."""

    # Add o processo de Factory do Pre processamento de Cidades
    factory = CheckingCityPreprocessingFactory()

    @staticmethod
    def skip_preprocessing(origin: int) -> bool:
        """Verifica se o pré-processamento deve ser ignorado."""
        return origin in hooks.CITY_TAPES

    def preprocessing(self, obj: Any) -> None:
        city_tracker: CityTracker = getattr(obj, 'dataclass')
        match city_tracker.origin:
            case origin if self.skip_preprocessing(origin):
                return
            case _:
                handler = self.factory.make(city_tracker.origin, city_tracker)
                handler.preprocessing()
