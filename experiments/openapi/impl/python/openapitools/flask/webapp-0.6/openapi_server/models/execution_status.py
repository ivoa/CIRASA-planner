from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class ExecutionStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, started=None, completed=None, status=None):  # noqa: E501
        """ExecutionStatus - a model defined in OpenAPI

        :param started: The started of this ExecutionStatus.  # noqa: E501
        :type started: datetime
        :param completed: The completed of this ExecutionStatus.  # noqa: E501
        :type completed: datetime
        :param status: The status of this ExecutionStatus.  # noqa: E501
        :type status: str
        """
        self.openapi_types = {
            'started': datetime,
            'completed': datetime,
            'status': str
        }

        self.attribute_map = {
            'started': 'started',
            'completed': 'completed',
            'status': 'status'
        }

        self._started = started
        self._completed = completed
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'ExecutionStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExecutionStatus of this ExecutionStatus.  # noqa: E501
        :rtype: ExecutionStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def started(self) -> datetime:
        """Gets the started of this ExecutionStatus.


        :return: The started of this ExecutionStatus.
        :rtype: datetime
        """
        return self._started

    @started.setter
    def started(self, started: datetime):
        """Sets the started of this ExecutionStatus.


        :param started: The started of this ExecutionStatus.
        :type started: datetime
        """

        self._started = started

    @property
    def completed(self) -> datetime:
        """Gets the completed of this ExecutionStatus.


        :return: The completed of this ExecutionStatus.
        :rtype: datetime
        """
        return self._completed

    @completed.setter
    def completed(self, completed: datetime):
        """Sets the completed of this ExecutionStatus.


        :param completed: The completed of this ExecutionStatus.
        :type completed: datetime
        """

        self._completed = completed

    @property
    def status(self) -> str:
        """Gets the status of this ExecutionStatus.

        Status code for the execution.   # noqa: E501

        :return: The status of this ExecutionStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this ExecutionStatus.

        Status code for the execution.   # noqa: E501

        :param status: The status of this ExecutionStatus.
        :type status: str
        """
        allowed_values = ["WAITING", "STANDUP", "RUNNING", "TEARDOWN", "COMPLETED", "CANCELLED", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status