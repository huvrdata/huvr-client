"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class ProjectsApiModule(BaseApiModule):
    
    def list(
        self,
        params=None,
        **kwargs
    ):
        """
        Returns an array projects.
        
        :param dict params: asset: string
        asset__asset_path_cache__path: string
        asset__type__in: string
        asset_condition: string
        asset_condition__in: string
        asset_parent__in: string
        asset_search: string
        assigned: string
        completed: string
        created_on: string
        crews__in: string
        crews__name: string
        descendants: string
        end: string
        event: string
        limit: integer
        management_company__in: string
        management_company__name: string
        name: string
        offset: integer
        ordering: string
        parent: string
        priority: string
        related_asset: string
        scope__selected_findings: string
        search: string
        start: string
        status: string
        type: string
        type__in: string
        type__name: string
        updated_on: string
        work_done_on: string
        
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
              $ref: '#/components/schemas/ProjectList'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_projects_list
        """
        return self.client.request(
            method="get",
            path=f"/api/projects/",
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
        
        :param dict json: $ref: '#/components/requestBodies/ProjectCreate'
        
        :returns: $ref: '#/components/schemas/ProjectDetail'
        
        https://docs.huvrdata.app/reference/api_projects_create
        """
        return self.client.request(
            method="post",
            path=f"/api/projects/",
            json=json,
            **kwargs,
        )
    
    def delete(
        self,
        json=None,
        **kwargs
    ):
        """
        View projects
        
        
        :param dict json: $ref: '#/components/requestBodies/ProjectDetail'
        
        https://docs.huvrdata.app/reference/api_projects_delete
        """
        return self.client.request(
            method="post",
            path=f"/api/projects/bulk-delete/",
            json=json,
            **kwargs,
        )
    
    def edit(
        self,
        json=None,
        **kwargs
    ):
        """
        View projects
        
        
        :param dict json: $ref: '#/components/requestBodies/ProjectDetail'
        
        https://docs.huvrdata.app/reference/api_projects_edit
        """
        return self.client.request(
            method="post",
            path=f"/api/projects/bulk-edit/",
            json=json,
            **kwargs,
        )
    
    def bulk_share(
        self,
        json=None,
        **kwargs
    ):
        """
        allow for bulk assignment/unassignment of multiple users to multiple projects
        
        :param dict json: $ref: '#/components/schemas/ProjectBulkShare'
        
        :returns: $ref: '#/components/schemas/ProjectListDetailed'
        
        https://docs.huvrdata.app/reference/api_projects_bulk_share
        """
        return self.client.request(
            method="post",
            path=f"/api/projects/bulk-share/",
            json=json,
            **kwargs,
        )
    
    def counts_by_status(
        self,
        params=None,
        **kwargs
    ):
        """
        View projects
        
        
        :param dict params: asset: string
        asset__asset_path_cache__path: string
        asset__type__in: string
        asset_condition: string
        asset_condition__in: string
        asset_parent__in: string
        asset_search: string
        assigned: string
        completed: string
        created_on: string
        crews__in: string
        crews__name: string
        descendants: string
        end: string
        event: string
        limit: integer
        management_company__in: string
        management_company__name: string
        name: string
        offset: integer
        ordering: string
        parent: string
        priority: string
        related_asset: string
        scope__selected_findings: string
        search: string
        start: string
        status: string
        type: string
        type__in: string
        type__name: string
        updated_on: string
        work_done_on: string
        
        :returns: $ref: '#/components/schemas/ProjectCountsByStatus'
        
        https://docs.huvrdata.app/reference/api_projects_counts_by_status
        """
        return self.client.request(
            method="get",
            path=f"/api/projects/counts-by-status/",
            params=params,
            **kwargs,
        )
    
    def list_detailed(
        self,
        params=None,
        **kwargs
    ):
        """
        Shows a detailed list or projects (slow).
        
        :param dict params: asset: string
        asset__asset_path_cache__path: string
        asset__type__in: string
        asset_condition: string
        asset_condition__in: string
        asset_parent__in: string
        asset_search: string
        assigned: string
        completed: string
        created_on: string
        crews__in: string
        crews__name: string
        descendants: string
        end: string
        event: string
        limit: integer
        management_company__in: string
        management_company__name: string
        name: string
        offset: integer
        ordering: string
        parent: string
        priority: string
        related_asset: string
        scope__selected_findings: string
        search: string
        start: string
        status: string
        type: string
        type__in: string
        type__name: string
        updated_on: string
        work_done_on: string
        
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
              $ref: '#/components/schemas/ProjectDetail'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_projects_list_detailed
        """
        return self.client.request(
            method="get",
            path=f"/api/projects/detailed/",
            params=params,
            **kwargs,
        )
    
    def read(
        self,
        id,
        **kwargs
    ):
        """
        Return the specific project
        :params id Project ID
        
        :returns: $ref: '#/components/schemas/ProjectDetail'
        
        https://docs.huvrdata.app/reference/api_projects_read
        """
        return self.client.request(
            method="get",
            path=f"/api/projects/{id}/",
            **kwargs,
        )
    
    def update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Project update. work_done_on is ignored if 'historical_project' is true
        
        :param dict json: $ref: '#/components/requestBodies/ProjectCreate'
        
        :returns: $ref: '#/components/schemas/ProjectDetail'
        
        https://docs.huvrdata.app/reference/api_projects_update
        """
        return self.client.request(
            method="put",
            path=f"/api/projects/{id}/",
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
        View projects
        
        
        :param dict json: $ref: '#/components/requestBodies/ProjectCreate'
        
        :returns: $ref: '#/components/schemas/ProjectCreate'
        
        https://docs.huvrdata.app/reference/api_projects_partial_update
        """
        return self.client.request(
            method="patch",
            path=f"/api/projects/{id}/",
            json=json,
            **kwargs,
        )
    
    def delete_alt(
        self,
        id,
        **kwargs
    ):
        """
        View projects
        
        https://docs.huvrdata.app/reference/api_projects_delete_alt
        """
        return self.client.request(
            method="delete",
            path=f"/api/projects/{id}/",
            **kwargs,
        )
    
    def asset_condition_read(
        self,
        id,
        **kwargs
    ):
        """
        Set the project asset condition, allow retrival of the project asset condition history
        
        :returns: items:
          $ref: '#/components/schemas/AssetConditionHistoryInline'
        type: array
        
        https://docs.huvrdata.app/reference/api_projects_asset-condition_read
        """
        return self.client.request(
            method="get",
            path=f"/api/projects/{id}/asset-condition/",
            **kwargs,
        )
    
    def asset_condition_create(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Set the project asset condition, allow retrival of the project asset condition history
        
        :param dict json: $ref: '#/components/schemas/AssetConditionChange'
        
        :returns: $ref: '#/components/schemas/AssetConditionHistoryInline'
        
        https://docs.huvrdata.app/reference/api_projects_asset-condition_create
        """
        return self.client.request(
            method="post",
            path=f"/api/projects/{id}/asset-condition/",
            json=json,
            **kwargs,
        )
    
    def asset_condition_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Set the project asset condition, allow retrival of the project asset condition history
        
        :param dict json: $ref: '#/components/requestBodies/ProjectDetail'
        
        :returns: $ref: '#/components/schemas/ProjectDetail'
        
        https://docs.huvrdata.app/reference/api_projects_asset-condition_update
        """
        return self.client.request(
            method="put",
            path=f"/api/projects/{id}/asset-condition/",
            json=json,
            **kwargs,
        )
    
    def export(
        self,
        id,
        **kwargs
    ):
        """
        Exports existing project in excel format.
        This is a simple helper API endpoint that is run by developers only
        as this process will probably (depending on data) outgrow an inline request.
        
        https://docs.huvrdata.app/reference/api_projects_export
        """
        return self.client.request(
            method="get",
            path=f"/api/projects/{id}/export/",
            **kwargs,
        )
    
    def location_summary(
        self,
        id,
        **kwargs
    ):
        """
        Location summary of the findings/defects for a given project
        
        :returns: $ref: '#/components/schemas/ProjectDetail'
        
        https://docs.huvrdata.app/reference/api_projects_location_summary
        """
        return self.client.request(
            method="get",
            path=f"/api/projects/{id}/location-summary/",
            **kwargs,
        )
    
    def status_read(
        self,
        id,
        **kwargs
    ):
        """
        Set the project status, allow retrieval of the project status history
        
        :returns: items:
          $ref: '#/components/schemas/ProjectStatus'
        type: array
        
        https://docs.huvrdata.app/reference/api_projects_status_read
        """
        return self.client.request(
            method="get",
            path=f"/api/projects/{id}/status/",
            **kwargs,
        )
    
    def status_create(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Set the project status, allow retrieval of the project status history
        
        :param dict json: $ref: '#/components/requestBodies/ProjectStatusEdit'
        
        :returns: $ref: '#/components/schemas/ProjectDetail'
        
        https://docs.huvrdata.app/reference/api_projects_status_create
        """
        return self.client.request(
            method="post",
            path=f"/api/projects/{id}/status/",
            json=json,
            **kwargs,
        )
    
    def status_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Set the project status, allow retrieval of the project status history
        
        :param dict json: $ref: '#/components/requestBodies/ProjectStatusEdit'
        
        :returns: $ref: '#/components/schemas/ProjectDetail'
        
        https://docs.huvrdata.app/reference/api_projects_status_update
        """
        return self.client.request(
            method="put",
            path=f"/api/projects/{id}/status/",
            json=json,
            **kwargs,
        )
    
    def watch(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Set the project watchers, allow retrival of the project watchers
        
        :param dict json: $ref: '#/components/schemas/ProjectShare'
        
        :returns: $ref: '#/components/schemas/ProjectDetail'
        
        https://docs.huvrdata.app/reference/api_projects_watch
        """
        return self.client.request(
            method="post",
            path=f"/api/projects/{id}/watch/",
            json=json,
            **kwargs,
        )
    