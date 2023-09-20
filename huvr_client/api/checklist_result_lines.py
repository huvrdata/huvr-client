"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class ChecklistResultLinesApiModule(BaseApiModule):
    def list(self, params=None, **kwargs):
        """
        Returns a list of ChecklistResultLines, supports various filters

        :param dict params: checklist: string
        checklist__project: string
        checklist__project__name: string
        id: string
        limit: integer
        line_key: string
        notes: string
        offset: integer
        ordering: string
        project: string
        search: string
        section_key: string
        template: string
        template__name: string
        template__version: string
        template_line: string
        template_line__description: string
        template_line__label: string
        template_line__section_description: string
        template_line__section_label: string
        template_line__type: string
        value: string

        :returns: properties:
          count:
            type: integer
          next:
            format: uri
            nullable: true
            type: string
          previous:
            format: uri
            nullable: true
            type: string
          results:
            items:
              $ref: '#/components/schemas/ChecklistResultLine'
            type: array
        required:
        - count
        - results
        type: object

        https://docs.huvrdata.app/reference/api_checklist-result-lines_list
        """
        return self.client.request(
            method="get",
            path=f"/api/checklist-result-lines/",
            params=params,
            **kwargs,
        )

    def read(self, id, **kwargs):
        """
        Return a single ChecklistResultLine by id
            `id` pattern: "{checklist_id}::{section_key}::{line_key}"
            for example: "24::my_section::my_line"

        :returns: $ref: '#/components/schemas/ChecklistResultLine'

        https://docs.huvrdata.app/reference/api_checklist-result-lines_read
        """
        return self.client.request(
            method="get",
            path=f"/api/checklist-result-lines/{id}/",
            **kwargs,
        )
