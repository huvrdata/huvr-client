"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class LibrariesApiModule(BaseApiModule):
    
    def list(
        self,
        params=None,
        **kwargs
    ):
        """
        GET /api/libraries/
        
        :param dict params: assigned: string
        limit: integer
        name: string
        offset: integer
        ordering: string
        system: string
        
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
              $ref: '#/components/schemas/Library'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_libraries_list
        """
        return self.client.request(
            method="get",
            path=f"/api/libraries/",
            params=params,
            **kwargs,
        )
    
    def read(
        self,
        id,
        **kwargs
    ):
        """
        View library media
        
        
        :returns: $ref: '#/components/schemas/Library'
        
        https://docs.huvrdata.app/reference/api_libraries_read
        """
        return self.client.request(
            method="get",
            path=f"/api/libraries/{id}/",
            **kwargs,
        )
    