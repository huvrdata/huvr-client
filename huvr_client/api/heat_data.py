"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class HeatDataApiModule(BaseApiModule):
    
    def list(
        self,
        params=None,
        **kwargs
    ):
        """
        Returns an array HEAT data
        
        :param dict params: billet_weight: string
        charge_weight: string
        created_on: string
        crew: string
        grade: string
        grade_type: string
        heat_number: string
        ladle: string
        limit: integer
        offset: integer
        ordering: string
        shift: string
        source__name: string
        tap_start: string
        
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
              $ref: '#/components/schemas/HeatData'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_heat-data_list
        """
        return self.client.request(
            method="get",
            path=f"/api/heat-data/",
            params=params,
            **kwargs,
        )
    
    def read(
        self,
        id,
        **kwargs
    ):
        """
        Return the specific HEAT data
        :params id HeatData ID
        
        :returns: $ref: '#/components/schemas/HeatData'
        
        https://docs.huvrdata.app/reference/api_heat-data_read
        """
        return self.client.request(
            method="get",
            path=f"/api/heat-data/{id}/",
            **kwargs,
        )
    