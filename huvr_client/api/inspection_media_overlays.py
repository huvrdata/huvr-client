"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class InspectionMediaOverlaysApiModule(BaseApiModule):
    def list(self, params=None, **kwargs):
        """
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
              $ref: '#/components/schemas/InspectionMediaOverlay'
            type: array
        required:
        - count
        - results
        type: object

        https://docs.huvrdata.app/reference/api_inspection-media-overlays_list
        """
        return self.client.request(
            method="get",
            path=f"/api/inspection-media-overlays/",
            params=params,
            **kwargs,
        )

    def create(self, json=None, **kwargs):
        """
        create inspection media overlay, the media object has to already exist.
        The defect can be passed in.

        :param dict json: $ref: '#/components/requestBodies/InspectionMediaOverlay'

        :returns: $ref: '#/components/schemas/InspectionMediaOverlay'

        https://docs.huvrdata.app/reference/api_inspection-media-overlays_create
        """
        return self.client.request(
            method="post",
            path=f"/api/inspection-media-overlays/",
            json=json,
            **kwargs,
        )

    def read(self, id, **kwargs):
        """
        :returns: $ref: '#/components/schemas/InspectionMediaOverlay'

        https://docs.huvrdata.app/reference/api_inspection-media-overlays_read
        """
        return self.client.request(
            method="get",
            path=f"/api/inspection-media-overlays/{id}/",
            **kwargs,
        )

    def update(self, id, json=None, **kwargs):
        """
        :param dict json: $ref: '#/components/requestBodies/InspectionMediaOverlay'

        :returns: $ref: '#/components/schemas/InspectionMediaOverlay'

        https://docs.huvrdata.app/reference/api_inspection-media-overlays_update
        """
        return self.client.request(
            method="put",
            path=f"/api/inspection-media-overlays/{id}/",
            json=json,
            **kwargs,
        )

    def partial_update(self, id, json=None, **kwargs):
        """
        :param dict json: $ref: '#/components/requestBodies/InspectionMediaOverlayCreate'

        :returns: $ref: '#/components/schemas/InspectionMediaOverlayCreate'

        https://docs.huvrdata.app/reference/api_inspection-media-overlays_partial_update
        """
        return self.client.request(
            method="patch",
            path=f"/api/inspection-media-overlays/{id}/",
            json=json,
            **kwargs,
        )

    def delete(self, id, **kwargs):
        """
        https://docs.huvrdata.app/reference/api_inspection-media-overlays_delete
        """
        return self.client.request(
            method="delete",
            path=f"/api/inspection-media-overlays/{id}/",
            **kwargs,
        )
