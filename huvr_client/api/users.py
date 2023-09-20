"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class UsersApiModule(BaseApiModule):
    
    def list(
        self,
        params=None,
        **kwargs
    ):
        """
        Returns an array users.
        
        :param dict params: company: string
        date_joined: string
        email: string
        is_active: string
        last_login: string
        limit: integer
        name: string
        offset: integer
        ordering: string
        roles: string
        search: string
        
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
              $ref: '#/components/schemas/User'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_users_list
        """
        return self.client.request(
            method="get",
            path=f"/api/users/",
            params=params,
            **kwargs,
        )
    
    def create(
        self,
        json=None,
        **kwargs
    ):
        """
        User create
        This function is used when creating a new user using the Users tab on the frontend
        
        :param dict json: $ref: '#/components/requestBodies/UserCreate'
        
        :returns: $ref: '#/components/schemas/User'
        
        https://docs.huvrdata.app/reference/api_users_create
        """
        return self.client.request(
            method="post",
            path=f"/api/users/",
            json=json,
            **kwargs,
        )
    
    def import_users(
        self,
        json=None,
        **kwargs
    ):
        """
        Pass a list of users addresses,
            sets the same roles/company for all
        
        :param dict json: $ref: '#/components/schemas/UserImport'
        
        https://docs.huvrdata.app/reference/api_users_import_users
        """
        return self.client.request(
            method="post",
            path=f"/api/users/import/",
            json=json,
            **kwargs,
        )
    
    def me_read(
        self,
        params=None,
        **kwargs
    ):
        """
        Return current user
        
        :param dict params: company: string
        date_joined: string
        email: string
        is_active: string
        last_login: string
        limit: integer
        name: string
        offset: integer
        ordering: string
        roles: string
        search: string
        
        :returns: $ref: '#/components/schemas/UserProfile'
        
        https://docs.huvrdata.app/reference/api_users_me_read
        """
        return self.client.request(
            method="get",
            path=f"/api/users/me/",
            params=params,
            **kwargs,
        )
    
    def me_create(
        self,
        json=None,
        **kwargs
    ):
        """
        Return current user
        
        :param dict json: $ref: '#/components/schemas/User'
        
        :returns: $ref: '#/components/schemas/User'
        
        https://docs.huvrdata.app/reference/api_users_me_create
        """
        return self.client.request(
            method="post",
            path=f"/api/users/me/",
            json=json,
            **kwargs,
        )
    
    def read(
        self,
        id,
        **kwargs
    ):
        """
        Return the specific user
        :params id User ID
        
        :returns: $ref: '#/components/schemas/User'
        
        https://docs.huvrdata.app/reference/api_users_read
        """
        return self.client.request(
            method="get",
            path=f"/api/users/{id}/",
            **kwargs,
        )
    
    def update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        User update
        
        :param dict json: $ref: '#/components/requestBodies/UserCreate'
        
        :returns: $ref: '#/components/schemas/User'
        
        https://docs.huvrdata.app/reference/api_users_update
        """
        return self.client.request(
            method="put",
            path=f"/api/users/{id}/",
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
        View users
        
        
        :param dict json: $ref: '#/components/requestBodies/UserCreate'
        
        :returns: $ref: '#/components/schemas/UserCreate'
        
        https://docs.huvrdata.app/reference/api_users_partial_update
        """
        return self.client.request(
            method="patch",
            path=f"/api/users/{id}/",
            json=json,
            **kwargs,
        )
    
    def delete(
        self,
        id,
        **kwargs
    ):
        """
        View users
        
        https://docs.huvrdata.app/reference/api_users_delete
        """
        return self.client.request(
            method="delete",
            path=f"/api/users/{id}/",
            **kwargs,
        )
    