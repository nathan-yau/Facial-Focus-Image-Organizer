from PyQt6.QtWidgets import QHBoxLayout

from sections.sections_creator import SectionsCreator


class OperationPageSectionsCreator(SectionsCreator):

    @staticmethod
    def _populate_section(outer_layout, widgets_function, object_name):
        layout = QHBoxLayout()
        widgets = widgets_function()
        for widget in widgets:
            layout.addWidget(widget)
        layout.setObjectName(object_name)
        outer_layout.addLayout(layout)

    def create_sections(self, outer_layout, widget_creator):
        self._populate_section(outer_layout, widget_creator.get_top_layout_widgets, "top_layout")
        self._populate_section(outer_layout, widget_creator.get_middle_layout_widgets, "middle_layout")
        self._populate_section(outer_layout, widget_creator.get_bottom_layout_widgets, "bottom_layout")