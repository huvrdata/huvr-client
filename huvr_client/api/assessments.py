"""
This file is automatically generated. Do not modify it manually.
"""

from .base_api_module import BaseApiModule


class AssessmentsApiModule(BaseApiModule):
    def list(self, params=None, **kwargs):
        """
        {
                "count": 1,
                "next": null,
                "previous": null,
                "results": [ { ... } ],
                "risk_matrix_rollup": [ ... ],
            }

        :param dict params: asset: string
        asset__asset_path_cache__path: string
        asset__descendants: string
        asset__id: string
        asset__type__in: string
        asset_path__endswith: string
        asset_path__icontains: string
        asset_path__startswith: string
        limit: integer
        offset: integer
        ordering: string
        risk_score__cof: string
        risk_score__display: string
        risk_score__pof: string
        status__in: string

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
              $ref: '#/components/schemas/AssessmentList'
            type: array
        required:
        - count
        - results
        type: object

        https://docs.huvrdata.app/reference/api_assessments_list
        """
        return self.client.request_json(
            method="get",
            path=f"/api/assessments/",
            params=params,
            **kwargs,
        )

    def read(self, id, **kwargs):
        """
        Return the specific Assessment
        :params id Assessment ID

        :returns: $ref: '#/components/schemas/AssessmentDetail'

        https://docs.huvrdata.app/reference/api_assessments_read
        """
        return self.client.request_json(
            method="get",
            path=f"/api/assessments/{id}/",
            **kwargs,
        )

    def revision(self, id, json=None, **kwargs):
        """
        :param dict json: $ref: '#/components/schemas/AssessmentDetail'

        :returns: $ref: '#/components/schemas/AssessmentDetail'

        https://docs.huvrdata.app/reference/api_assessments_revision
        """
        return self.client.request_json(
            method="post",
            path=f"/api/assessments/{id}/revision/",
            json=json,
            **kwargs,
        )
