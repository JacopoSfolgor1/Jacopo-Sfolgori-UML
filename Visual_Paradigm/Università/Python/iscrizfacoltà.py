from custom_types import IntGE1088

class iscriz_facoltà:

    _anno_iscrizione: IntGE1088 # noto alla nascita

    def __init__(self, anno_iscrizione: IntGE1088) -> None:
        self.set_anno_iscrizione(anno_iscrizione)

    def anno_iscrizione(self) -> IntGE1088:
        return self._anno_iscrizione
    
    def set_anno_iscrizione(self, ann: IntGE1088) -> None:
        self._anno_iscrizione: IntGE1088 = ann