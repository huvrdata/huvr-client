"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class ProjectTypesApiModule(BaseApiModule):
    
    def list(
        self,
        params=None,
        **kwargs
    ):
        """
        Returns an array project types.
        
        :param dict params: in_use: string
        is_active: string
        limit: integer
        name: string
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
              $ref: '#/components/schemas/ProjectTypeDetail'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_project-types_list
        """
        return self.client.request(
            method="get",
            path=f"/api/project-types/",
            params=params,
            **kwargs,
        )
    
    def create(
        self,
        json=None,
        **kwargs
    ):
        """
        accept a flat object for create, return nested detail object
        
        :param dict json: $ref: '#/components/requestBodies/ProjectTypeCreate'
        
        :returns: $ref: '#/components/schemas/ProjectTypeDetail'
        
        https://docs.huvrdata.app/reference/api_project-types_create
        """
        return self.client.request(
            method="post",
            path=f"/api/project-types/",
            json=json,
            **kwargs,
        )
    
    def read(
        self,
        id,
        **kwargs
    ):
        """
        Return the specific project type
        :params id project_type ID
        
        :returns: $ref: '#/components/schemas/ProjectTypeDetail'
        
        https://docs.huvrdata.app/reference/api_project-types_read
        """
        return self.client.request(
            method="get",
            path=f"/api/project-types/{id}/",
            **kwargs,
        )
    
    def update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Project Type endpoint
        
        
        :param dict json: $ref: '#/components/requestBodies/ProjectTypeCreate'
        
        :returns: $ref: '#/components/schemas/ProjectTypeDetail'
        
        https://docs.huvrdata.app/reference/api_project-types_update
        """
        return self.client.request(
            method="put",
            path=f"/api/project-types/{id}/",
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
        Project Type endpoint
        
        
        :param dict json: $ref: '#/components/requestBodies/ProjectTypeCreate'
        
        :returns: $ref: '#/components/schemas/ProjectTypeCreate'
        
        https://docs.huvrdata.app/reference/api_project-types_partial_update
        """
        return self.client.request(
            method="patch",
            path=f"/api/project-types/{id}/",
            json=json,
            **kwargs,
        )
    
    def delete(
        self,
        id,
        **kwargs
    ):
        """
        Project Type endpoint
        
        https://docs.huvrdata.app/reference/api_project-types_delete
        """
        return self.client.request(
            method="delete",
            path=f"/api/project-types/{id}/",
            **kwargs,
        )
    