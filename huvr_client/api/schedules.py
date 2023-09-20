"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class SchedulesApiModule(BaseApiModule):
    
    def events_list(
        self,
        params=None,
        **kwargs
    ):
        """
        Returns an array of schedule events.
        
        :param dict params: asset: string
        asset__asset_path_cache__path: string
        crew: string
        crew__name: string
        descendants: string
        end: string
        limit: integer
        name: string
        offset: integer
        ordering: string
        plan: string
        quick_date: string
        search: string
        start: string
        
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
              $ref: '#/components/schemas/ScheduleEvent'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_schedule_events_list
        """
        return self.client.request(
            method="get",
            path=f"/api/schedule/events/",
            params=params,
            **kwargs,
        )
    
    def events_create(
        self,
        json=None,
        **kwargs
    ):
        """
        :param dict json: $ref: '#/components/requestBodies/ScheduleEvent'
        
        :returns: $ref: '#/components/schemas/ScheduleEvent'
        
        https://docs.huvrdata.app/reference/api_schedule_events_create
        """
        return self.client.request(
            method="post",
            path=f"/api/schedule/events/",
            json=json,
            **kwargs,
        )
    
    def events_read(
        self,
        id,
        **kwargs
    ):
        """
        Return the specific schedule event
        :params id schedule event ID
        
        :returns: $ref: '#/components/schemas/ScheduleEvent'
        
        https://docs.huvrdata.app/reference/api_schedule_events_read
        """
        return self.client.request(
            method="get",
            path=f"/api/schedule/events/{id}/",
            **kwargs,
        )
    
    def events_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        :param dict json: $ref: '#/components/requestBodies/ScheduleEvent'
        
        :returns: $ref: '#/components/schemas/ScheduleEvent'
        
        https://docs.huvrdata.app/reference/api_schedule_events_update
        """
        return self.client.request(
            method="put",
            path=f"/api/schedule/events/{id}/",
            json=json,
            **kwargs,
        )
    
    def events_partial_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        :param dict json: $ref: '#/components/requestBodies/ScheduleEvent'
        
        :returns: $ref: '#/components/schemas/ScheduleEvent'
        
        https://docs.huvrdata.app/reference/api_schedule_events_partial_update
        """
        return self.client.request(
            method="patch",
            path=f"/api/schedule/events/{id}/",
            json=json,
            **kwargs,
        )
    
    def events_delete(
        self,
        id,
        **kwargs
    ):
        """
        https://docs.huvrdata.app/reference/api_schedule_events_delete
        """
        return self.client.request(
            method="delete",
            path=f"/api/schedule/events/{id}/",
            **kwargs,
        )
    
    def plan_work_list(
        self,
        params=None,
        **kwargs
    ):
        """
        Returns an array of schedule plan work items
        
        :param dict params: limit: integer
        offset: integer
        ordering: string
        plan: string
        
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
              $ref: '#/components/schemas/SchedulePlanWork'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_schedule_plan-work_list
        """
        return self.client.request(
            method="get",
            path=f"/api/schedule/plan-work/",
            params=params,
            **kwargs,
        )
    
    def plan_work_create(
        self,
        json=None,
        **kwargs
    ):
        """
        View schedule work plan
        
        
        :param dict json: $ref: '#/components/requestBodies/SchedulePlanWorkCreate'
        
        :returns: $ref: '#/components/schemas/SchedulePlanWork'
        
        https://docs.huvrdata.app/reference/api_schedule_plan-work_create
        """
        return self.client.request(
            method="post",
            path=f"/api/schedule/plan-work/",
            json=json,
            **kwargs,
        )
    
    def plan_work_read(
        self,
        id,
        **kwargs
    ):
        """
        Return the specific schedule plan work
        :params id schedule plan work ID
        
        :returns: $ref: '#/components/schemas/SchedulePlanWork'
        
        https://docs.huvrdata.app/reference/api_schedule_plan-work_read
        """
        return self.client.request(
            method="get",
            path=f"/api/schedule/plan-work/{id}/",
            **kwargs,
        )
    
    def plan_work_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Schedule Plan update
        
        :param dict json: $ref: '#/components/requestBodies/SchedulePlanWorkCreate'
        
        :returns: $ref: '#/components/schemas/SchedulePlan'
        
        https://docs.huvrdata.app/reference/api_schedule_plan-work_update
        """
        return self.client.request(
            method="put",
            path=f"/api/schedule/plan-work/{id}/",
            json=json,
            **kwargs,
        )
    
    def plan_work_partial_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        View schedule work plan
        
        
        :param dict json: $ref: '#/components/requestBodies/SchedulePlanWorkCreate'
        
        :returns: $ref: '#/components/schemas/SchedulePlanWorkCreate'
        
        https://docs.huvrdata.app/reference/api_schedule_plan-work_partial_update
        """
        return self.client.request(
            method="patch",
            path=f"/api/schedule/plan-work/{id}/",
            json=json,
            **kwargs,
        )
    
    def plan_work_delete(
        self,
        id,
        **kwargs
    ):
        """
        View schedule work plan
        
        https://docs.huvrdata.app/reference/api_schedule_plan-work_delete
        """
        return self.client.request(
            method="delete",
            path=f"/api/schedule/plan-work/{id}/",
            **kwargs,
        )
    
    def plans_list(
        self,
        params=None,
        **kwargs
    ):
        """
        Returns an array of schedule plans
        
        :param dict params: limit: integer
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
              $ref: '#/components/schemas/SchedulePlan'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_schedule_plans_list
        """
        return self.client.request(
            method="get",
            path=f"/api/schedule/plans/",
            params=params,
            **kwargs,
        )
    
    def plans_create(
        self,
        json=None,
        **kwargs
    ):
        """
        View schedule plan
        
        
        :param dict json: $ref: '#/components/requestBodies/SchedulePlanCreate'
        
        :returns: $ref: '#/components/schemas/SchedulePlan'
        
        https://docs.huvrdata.app/reference/api_schedule_plans_create
        """
        return self.client.request(
            method="post",
            path=f"/api/schedule/plans/",
            json=json,
            **kwargs,
        )
    
    def plans_read(
        self,
        id,
        **kwargs
    ):
        """
        Return the specific schedule plan
        :params id schedule plan ID
        
        :returns: $ref: '#/components/schemas/SchedulePlan'
        
        https://docs.huvrdata.app/reference/api_schedule_plans_read
        """
        return self.client.request(
            method="get",
            path=f"/api/schedule/plans/{id}/",
            **kwargs,
        )
    
    def plans_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Schedule Plan update
        
        :param dict json: $ref: '#/components/requestBodies/SchedulePlanCreate'
        
        :returns: $ref: '#/components/schemas/SchedulePlan'
        
        https://docs.huvrdata.app/reference/api_schedule_plans_update
        """
        return self.client.request(
            method="put",
            path=f"/api/schedule/plans/{id}/",
            json=json,
            **kwargs,
        )
    
    def plans_partial_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        View schedule plan
        
        
        :param dict json: $ref: '#/components/requestBodies/SchedulePlanCreate'
        
        :returns: $ref: '#/components/schemas/SchedulePlanCreate'
        
        https://docs.huvrdata.app/reference/api_schedule_plans_partial_update
        """
        return self.client.request(
            method="patch",
            path=f"/api/schedule/plans/{id}/",
            json=json,
            **kwargs,
        )
    
    def plans_delete(
        self,
        id,
        **kwargs
    ):
        """
        View schedule plan
        
        https://docs.huvrdata.app/reference/api_schedule_plans_delete
        """
        return self.client.request(
            method="delete",
            path=f"/api/schedule/plans/{id}/",
            **kwargs,
        )
    
    def plans_generate_events_create(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Generate Events for a SchedulePlan
        
        :param dict json: $ref: '#/components/requestBodies/SchedulePlan'
        
        :returns: $ref: '#/components/schemas/SchedulePlanGenerateEvents'
        
        https://docs.huvrdata.app/reference/api_schedule_plans_generate-events_create
        """
        return self.client.request(
            method="post",
            path=f"/api/schedule/plans/{id}/generate-events/",
            json=json,
            **kwargs,
        )
    
    def plans_generate_events_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Generate Events for a SchedulePlan
        
        :param dict json: $ref: '#/components/requestBodies/SchedulePlan'
        
        :returns: $ref: '#/components/schemas/SchedulePlanGenerateEvents'
        
        https://docs.huvrdata.app/reference/api_schedule_plans_generate-events_update
        """
        return self.client.request(
            method="put",
            path=f"/api/schedule/plans/{id}/generate-events/",
            json=json,
            **kwargs,
        )
    
    def tasks_list(
        self,
        params=None,
        **kwargs
    ):
        """
        Returns an array of schedule task.
        
        :param dict params: assigned: string
        current: string
        done: string
        event: string
        limit: integer
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
              $ref: '#/components/schemas/ScheduleTask'
            type: array
        required:
        - count
        - results
        type: object
        
        https://docs.huvrdata.app/reference/api_schedule_tasks_list
        """
        return self.client.request(
            method="get",
            path=f"/api/schedule/tasks/",
            params=params,
            **kwargs,
        )
    
    def tasks_read(
        self,
        id,
        **kwargs
    ):
        """
        Return the specific schedule task
        :params id schedule task ID
        
        :returns: $ref: '#/components/schemas/ScheduleTask'
        
        https://docs.huvrdata.app/reference/api_schedule_tasks_read
        """
        return self.client.request(
            method="get",
            path=f"/api/schedule/tasks/{id}/",
            **kwargs,
        )
    
    def tasks_update(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        :param dict json: $ref: '#/components/requestBodies/ScheduleTask'
        
        :returns: $ref: '#/components/schemas/ScheduleTask'
        
        https://docs.huvrdata.app/reference/api_schedule_tasks_update
        """
        return self.client.request(
            method="put",
            path=f"/api/schedule/tasks/{id}/",
            json=json,
            **kwargs,
        )
    
    def tasks_delete(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        :param dict json: $ref: '#/components/requestBodies/ScheduleTask'
        
        :returns: $ref: '#/components/schemas/ScheduleTask'
        
        https://docs.huvrdata.app/reference/api_schedule_tasks_delete
        """
        return self.client.request(
            method="post",
            path=f"/api/schedule/tasks/{id}/delete/",
            json=json,
            **kwargs,
        )
    
    def tasks_reconcile(
        self,
        id,
        json=None,
        **kwargs
    ):
        """
        Look for work that matches the schedule task.
        
        :param dict json: $ref: '#/components/requestBodies/ScheduleTask'
        
        :returns: $ref: '#/components/schemas/ScheduleTaskReconcile'
        
        https://docs.huvrdata.app/reference/api_schedule_tasks_reconcile
        """
        return self.client.request(
            method="post",
            path=f"/api/schedule/tasks/{id}/reconcile/",
            json=json,
            **kwargs,
        )
    