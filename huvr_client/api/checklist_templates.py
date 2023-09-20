"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class ChecklistTemplatesApiModule(BaseApiModule):
    
    def list(
        self,
        params=None,
        **kwargs
    ):
        """
        Returns an array of checklist templates.
        
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
              $ref: '#/components/schemas/ChecklistTemplateList'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_checklist-templates_list
        """
        return self.client.request(
            method="get",
            path=f"/api/checklist-templates/",
            params=params,
            **kwargs,
        )
    
    def create(
        self,
        json=None,
        **kwargs
    ):
        """
        View Checklist Templates
        
        
        :param dict json: $ref: '#/components/requestBodies/ChecklistTemplate'
        
        :returns: $ref: '#/components/schemas/ChecklistTemplate'
        
        https://docs.huvrdata.app/reference/api_checklist-templates_create
        """
        return self.client.request(
            method="post",
            path=f"/api/checklist-templates/",
            json=json,
            **kwargs,
        )
    
    def import_template(
        self,
        json=None,
        **kwargs
    ):
        """
        Import a checklist template, this endpoint can simply do the conversion
        from excel to JSON. Or it can create/update the template in a single request.
        The `action` parameter switches between import/convert.
        If the `id` is passed in it will attempt to update the exisiting template.
        
        :param dict json: $ref: '#/components/requestBodies/ChecklistTemplate'
        
        :returns: $ref: '#/components/schemas/ChecklistInstance'
        
        https://docs.huvrdata.app/reference/api_checklist-templates_import_template
        """
        return self.client.request(
            method="post",
            path=f"/api/checklist-templates/import-template/",
            json=json,
            **kwargs,
        )
    
    def read(
        self,
        id,
        **kwargs
    ):
        """
        Return the specific Checklist Templates
        :params id template ID
        
        :returns: $ref: '#/components/schemas/ChecklistTemplate'
        
        https://docs.huvrdata.app/reference/api_checklist-templates_read
        """
        return self.client.request(
            method="get",
            path=f"/api/checklist-templates/{id}/",
            **kwargs,
        )
    
    def update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        View Checklist Templates
        
        
        :param dict json: $ref: '#/components/requestBodies/ChecklistTemplate'
        
        :returns: $ref: '#/components/schemas/ChecklistTemplate'
        
        https://docs.huvrdata.app/reference/api_checklist-templates_update
        """
        return self.client.request(
            method="put",
            path=f"/api/checklist-templates/{id}/",
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
        View Checklist Templates
        
        
        :param dict json: $ref: '#/components/requestBodies/ChecklistTemplate'
        
        :returns: $ref: '#/components/schemas/ChecklistTemplate'
        
        https://docs.huvrdata.app/reference/api_checklist-templates_partial_update
        """
        return self.client.request(
            method="patch",
            path=f"/api/checklist-templates/{id}/",
            json=json,
            **kwargs,
        )
    
    def delete(
        self,
        id,
        **kwargs
    ):
        """
        View Checklist Templates
        
        https://docs.huvrdata.app/reference/api_checklist-templates_delete
        """
        return self.client.request(
            method="delete",
            path=f"/api/checklist-templates/{id}/",
            **kwargs,
        )
    
    def export_template(
        self,
        id,
        **kwargs
    ):
        """
        Exports existing checklist template in excel format.
        
        https://docs.huvrdata.app/reference/api_checklist-templates_export_template
        """
        return self.client.request(
            method="get",
            path=f"/api/checklist-templates/{id}/export-template/",
            **kwargs,
        )
    