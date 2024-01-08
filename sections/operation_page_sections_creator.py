from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from sections.sections_creator import SectionsCreator


class OperationPageSectionsCreator(SectionsCreator):

    def add_subsection_to_layout(self, layout, widgets):
        for widget in widgets:
            if isinstance(widget, list):
                sub_layout = QVBoxLayout() if layout.__class__ == QHBoxLayout else QHBoxLayout()
                self.add_subsection_to_layout(sub_layout, widget)
                layout.addLayout(sub_layout)
            else:
                layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignHCenter)

    def _populate_section(self, outer_layout, widgets_function, object_name):
        sub_section = widgets_function()
        inner_layout = QHBoxLayout()
        for index, section in enumerate(sub_section):
            if index:
                sub_section_layout = QVBoxLayout()
            else:
                sub_section_layout = QVBoxLayout()
            if isinstance(section, list):
                self.add_subsection_to_layout(sub_section_layout, section)
                inner_layout.addLayout(sub_section_layout)
            else:
                inner_layout.addWidget(section, alignment=Qt.AlignmentFlag.AlignHCenter)
            inner_layout.setContentsMargins(20, 20, 20, 20)
            inner_layout.setObjectName(object_name)

        outer_layout.addLayout(inner_layout)

    def _populate_to_section(self, outer_layout, widgets_function, object_name):
        sub_section = widgets_function()
        inner_layout = QVBoxLayout()
        for index, section in enumerate(sub_section):
            if index:
                sub_section_layout = QHBoxLayout()
            else:
                sub_section_layout = QHBoxLayout()
            if isinstance(section, list):
                self.add_subsection_to_layout(sub_section_layout, section)
                inner_layout.addLayout(sub_section_layout)
            else:
                inner_layout.addWidget(section)
        inner_layout.setObjectName(object_name)
        outer_layout.addLayout(inner_layout)

    def create_sections(self, outer_layout, widget_creator):
        self._populate_section(outer_layout, widget_creator.get_top_layout_widgets, "top_layout")
        self._populate_section(outer_layout, widget_creator.get_middle_layout_widgets, "middle_layout")