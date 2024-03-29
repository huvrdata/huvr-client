"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class ChecklistTemplatesFillableApiModule(BaseApiModule):
    def list(self, params=None, **kwargs):
        """
        Returns an array of checklist templates ready to be used by the client.

        :param dict params: categories: string
        in_use: string
        limit: integer
        name: string
        offset: integer
        ordering: string
        schema_version: string
        state: string
        type: string

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
              $ref: '#/components/schemas/ChecklistTemplateFillable'
            type: array
        required:
        - count
        - results
        type: object

        https://docs.huvrdata.app/reference/api_checklist-templates-fillable_list
        """
        return self.client.request_json(
            method="get",
            path=f"/api/checklist-templates-fillable/",
            params=params,
            **kwargs,
        )

    def read(self, id, **kwargs):
        """
        Return the specific Checklist Templates
        :params id template ID

        :returns: $ref: '#/components/schemas/ChecklistTemplateFillable'

        https://docs.huvrdata.app/reference/api_checklist-templates-fillable_read
        """
        return self.client.request_json(
            method="get",
            path=f"/api/checklist-templates-fillable/{id}/",
            **kwargs,
        )
