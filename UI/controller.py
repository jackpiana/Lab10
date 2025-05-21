import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._stato = None

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
            self._view._txt_result.controls.append(ft.Text(f"Componenti connesse: {self._model.get_componenti_connesse()}"))
            stati = list(self._model._grafo.nodes)
            stati.sort()
            for stato in stati:
                self._view._txt_result.controls.append(ft.Text(f"{stato} --- "
                                                               f" stati confinanti: "
                                                               f"{self._model._grafo.degree(stato)}"))
            self.fill_dd()
            self._view._page.update()

        except ValueError:
            self._view.create_alert("inserire un anno !")

    def handleRaggiungibili(self):
        node = self._stato
        if node:
            self._view._txt_result.clean()
            raggiungibili = self._model.get_reachable_nodes(node)
            self._view._txt_result.controls.append(ft.Text(f"stati raggiungibili da {node}"))
            for n in raggiungibili:
                self._view._txt_result.controls.append(ft.Text(f"{n}"))
            self._view._page.update()
        else:
            self._view.create_alert("selezionare uno stato !")


    def fill_dd(self):
        stati = self._model._grafo.nodes
        for stato in stati:
            self._view._ddMenu.options.append(ft.dropdown.Option(key=stato.CCode,
                                                                   text=stato.StateNme,
                                                                   data=stato,
                                                                   on_click=self.read_stato))

    def read_stato(self, e):
        self._stato = e.control.data
        print(self._stato)


