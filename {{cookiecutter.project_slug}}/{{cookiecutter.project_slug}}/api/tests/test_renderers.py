import json
from unittest.mock import Mock

import pytest
from rest_framework import status

from {{ cookiecutter.project_slug }}.api.renderers import MyJSONRenderer
from {{ cookiecutter.project_slug }}.api.renderers import get_status


class TestJSONRenderer:
    @pytest.fixture()
    def renderer(self):
        return MyJSONRenderer()

    def test_render(self, renderer):
        # Create a mock response with a client error status code
        response = Mock()
        response.status_code = status.HTTP_200_OK

        # Create a mock renderer context with the mock response
        renderer_context = {"response": response}

        data = {"foo": "bar"}

        rendered_data = renderer.render(data, renderer_context=renderer_context)

        rendered_data = json.loads(rendered_data)

        assert "errors" not in rendered_data
        assert rendered_data["data"] == data
        assert rendered_data["code"] == response.status_code
        assert rendered_data["status"] == get_status(response.status_code)

    def test_render_errors(self, renderer):
        # Create a mock response with a client error status code
        response = Mock()
        response.status_code = status.HTTP_404_NOT_FOUND

        # Create a mock renderer context with the mock response
        renderer_context = {"response": response}

        data = {"detail": "Not found."}

        rendered_data = renderer.render(data, renderer_context=renderer_context)

        rendered_data = json.loads(rendered_data)

        assert rendered_data["errors"] == data
        assert rendered_data["code"] == response.status_code
        assert rendered_data["status"] == get_status(response.status_code)
