"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class PagesApiModule(BaseApiModule):
    def list(self, params=None, **kwargs):
        """
        Returns an array Pages.

        :param dict params: limit: integer
        offset: integer
        ordering: string

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
              $ref: '#/components/schemas/PageList'
            type: array
        required:
        - count
        - results
        type: object

        https://docs.huvrdata.app/reference/api_pages_list
        """
        return self.client.request_json(
            method="get",
            path=f"/api/pages/",
            params=params,
            **kwargs,
        )

    def retrieve_by_path(self, path, params=None, **kwargs):
        """
        The path will have to be url-encoded when coming in.

        :param dict params: limit: integer
        offset: integer
        ordering: string

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
              $ref: '#/components/schemas/PageDetail'
            type: array
        required:
        - count
        - results
        type: object

        https://docs.huvrdata.app/reference/api_pages_retrieve_by_path
        """
        return self.client.request_json(
            method="get",
            path=f"/api/pages/by-path/{path}/",
            params=params,
            **kwargs,
        )

    def read(self, id, **kwargs):
        """
        Return the specific Page
        :params id Page ID

        :returns: $ref: '#/components/schemas/PageDetail'

        https://docs.huvrdata.app/reference/api_pages_read
        """
        return self.client.request_json(
            method="get",
            path=f"/api/pages/{id}/",
            **kwargs,
        )
