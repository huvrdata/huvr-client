"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class CrewsApiModule(BaseApiModule):
    def list(self, params=None, **kwargs):
        """
        Returns an array of Crew objectss

        :param dict params: company: string
        is_active: string
        limit: integer
        name: string
        offset: integer
        ordering: string
        user: string

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
              $ref: '#/components/schemas/CrewDetail'
            type: array
        required:
        - count
        - results
        type: object

        https://docs.huvrdata.app/reference/api_crews_list
        """
        return self.client.request_json(
            method="get",
            path=f"/api/crews/",
            params=params,
            **kwargs,
        )

    def create(self, json=None, **kwargs):
        """
        accept a flat object for create, return nested detail object

        :param dict json: $ref: '#/components/schemas/CrewCreate'

        :returns: $ref: '#/components/schemas/CrewDetail'

        https://docs.huvrdata.app/reference/api_crews_create
        """
        return self.client.request_json(
            method="post",
            path=f"/api/crews/",
            json=json,
            **kwargs,
        )

    def read(self, id, **kwargs):
        """
        Return the specific Crew
        :params id crew ID

        :returns: $ref: '#/components/schemas/CrewDetail'

        https://docs.huvrdata.app/reference/api_crews_read
        """
        return self.client.request_json(
            method="get",
            path=f"/api/crews/{id}/",
            **kwargs,
        )

    def update(self, id, json=None, **kwargs):
        """
        Crew update. Company is ignored on updates

        :param dict json: $ref: '#/components/requestBodies/CrewUpdate'

        :returns: $ref: '#/components/schemas/CrewDetail'

        https://docs.huvrdata.app/reference/api_crews_update
        """
        return self.client.request_json(
            method="put",
            path=f"/api/crews/{id}/",
            json=json,
            **kwargs,
        )

    def partial_update(self, id, json=None, **kwargs):
        """
        Crew endpoint


        :param dict json: $ref: '#/components/requestBodies/CrewUpdate'

        :returns: $ref: '#/components/schemas/CrewUpdate'

        https://docs.huvrdata.app/reference/api_crews_partial_update
        """
        return self.client.request_json(
            method="patch",
            path=f"/api/crews/{id}/",
            json=json,
            **kwargs,
        )

    def delete(self, id, **kwargs):
        """
        Crew endpoint

        https://docs.huvrdata.app/reference/api_crews_delete
        """
        return self.client.request_json(
            method="delete",
            path=f"/api/crews/{id}/",
            **kwargs,
        )
