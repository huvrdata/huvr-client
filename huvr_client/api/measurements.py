"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class MeasurementsApiModule(BaseApiModule):
    
    def list(
        self,
        params=None,
        **kwargs
    ):
        """
        :param dict params: cml: string
        cml__name: string
        limit: integer
        measurement_offset: string
        offset: integer
        ordering: string
        project: string
        search: string
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
              $ref: '#/components/schemas/MeasurementList'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_measurements_list
        """
        return self.client.request(
            method="get",
            path=f"/api/measurements/",
            params=params,
            **kwargs,
        )
    
    def create(
        self,
        json=None,
        **kwargs
    ):
        """
        create Measurement
        
        :param dict json: $ref: '#/components/requestBodies/MeasurementCreate'
        
        :returns: $ref: '#/components/schemas/Measurement'
        
        https://docs.huvrdata.app/reference/api_measurements_create
        """
        return self.client.request(
            method="post",
            path=f"/api/measurements/",
            json=json,
            **kwargs,
        )
    
    def delete(
        self,
        json=None,
        **kwargs
    ):
        """
        :param dict json: $ref: '#/components/schemas/Measurement'
        
        https://docs.huvrdata.app/reference/api_measurements_delete
        """
        return self.client.request(
            method="post",
            path=f"/api/measurements/bulk-delete/",
            json=json,
            **kwargs,
        )
    
    def import_measurements(
        self,
        json=None,
        **kwargs
    ):
        """
        import measurements
        if asset_path is passed in. We will walk the downtree assets
        looking for matching CML's
        
        :param dict json: $ref: '#/components/schemas/MeasurementImport'
        
        :returns: $ref: '#/components/schemas/Measurement'
        
        https://docs.huvrdata.app/reference/api_measurements_import_measurements
        """
        return self.client.request(
            method="post",
            path=f"/api/measurements/import/",
            json=json,
            **kwargs,
        )
    
    def read(
        self,
        id,
        **kwargs
    ):
        """
        :returns: $ref: '#/components/schemas/Measurement'
        
        https://docs.huvrdata.app/reference/api_measurements_read
        """
        return self.client.request(
            method="get",
            path=f"/api/measurements/{id}/",
            **kwargs,
        )
    
    def update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        :param dict json: $ref: '#/components/requestBodies/MeasurementCreate'
        
        :returns: $ref: '#/components/schemas/Measurement'
        
        https://docs.huvrdata.app/reference/api_measurements_update
        """
        return self.client.request(
            method="put",
            path=f"/api/measurements/{id}/",
            json=json,
            **kwargs,
        )
    
    def partial_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        :param dict json: $ref: '#/components/requestBodies/MeasurementCreate'
        
        :returns: $ref: '#/components/schemas/MeasurementCreate'
        
        https://docs.huvrdata.app/reference/api_measurements_partial_update
        """
        return self.client.request(
            method="patch",
            path=f"/api/measurements/{id}/",
            json=json,
            **kwargs,
        )
    
    def delete_alt(
        self,
        id,
        **kwargs
    ):
        """
        https://docs.huvrdata.app/reference/api_measurements_delete_alt
        """
        return self.client.request(
            method="delete",
            path=f"/api/measurements/{id}/",
            **kwargs,
        )
    