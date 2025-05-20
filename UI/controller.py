import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        try:
            anno = int(anno)
            if not (anno <= 2006 and anno >= 1816):
                self._view.create_alert("inserire un anno compreso tra il 1816 e il 2006 !")
                return
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(ft.Text(f"Anno selezionato: {anno}"))
            self._model.buildGraph(anno)
            stati = list(self._model._grafo.nodes)
            for stato in stati:
                self._view._txt_result.controls.append(ft.Text(f"{stato} --- "
                                                               f" stati confinanti: "
                                                               f"{self._model._grafo.degree(stato)}"))
            self._view._page.update()

        except ValueError:
            self._view.create_alert("inserire un anno !")

