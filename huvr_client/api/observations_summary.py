"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class ObservationsSummaryApiModule(BaseApiModule):
    def list(self, params=None, **kwargs):
        """
        The Observations API returns a summary/counts of checklist instance data
        based on the grouping of the checklist template. The templates are
        typically filtered by a category. (i.e. Safety)



        :param dict params: asset: string
        asset__asset_path_cache__path: string
        asset__id: string
        created_by: string
        created_by_me: string
        created_on: string
        descendants: string
        labels: string
        limit: integer
        offset: integer
        ordering: string
        project: string
        recent: string
        search: string
        tasks: string
        template: string
        template__categories: string
        template__id__in: string
        template__name: string
        template__type: string

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
              $ref: '#/components/schemas/ChecklistSummary'
            type: array
        required:
        - count
        - results
        type: object

        https://docs.huvrdata.app/reference/api_observations-summary_list
        """
        return self.client.request_json(
            method="get",
            path=f"/api/observations-summary/",
            params=params,
            **kwargs,
        )
