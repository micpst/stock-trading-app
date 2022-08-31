from typing import Any


class UpdateMixin:
    def update(self, **kwargs: Any) -> None:
        if self._state.adding:
            raise self.DoesNotExist
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save(update_fields=kwargs.keys())
