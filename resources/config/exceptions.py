class NoConfigFile(Exception): ...
class KeyUndefined(Exception): ...

class InvalidAnnotation(Exception):
    def __init__(self, config_class: type, annotation_type):
        self.annotation_type = annotation_type
        super().__init__(
            f"{config_class.__name__} can't have annotation {annotation_type}, see doc"
        )
