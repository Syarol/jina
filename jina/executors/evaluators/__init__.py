__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from typing import Any

from .running_stats import RunningStats
from .. import BaseExecutor
from ..compound import CompoundExecutor


class BaseEvaluator(BaseExecutor):
    """A :class:`BaseEvaluator` is used to evaluate different messages coming from any kind of executor
    """

    def post_init(self):
        super().post_init()
        self._running_stats = RunningStats()

    @property
    def metric(self) -> str:
        """Get the name of the evaluation metric """
        raise NotImplementedError

    def evaluate(self, actual: Any, desired: Any, *args, **kwargs) -> float:
        raise NotImplementedError

    @property
    def mean(self) -> float:
        return self._running_stats.mean

    @property
    def std(self) -> float:
        return self._running_stats.std

    @property
    def variance(self) -> float:
        return self._running_stats.variance


class FileBasedEvaluator(CompoundExecutor):
    """A Frequently used pattern for combining A :class:`BinaryPbIndexer` and :class:`BaseEvaluator`.
     It will be equipped with predefined ``requests.on`` behaviors:

         -  At evaluation time(query or index)
             - 1. Checks for the incoming document, gets its value from the `BinaryPbIndexer` and fills the `groundtruth of the request
             - 2. Filter the documents that do not have a corresponding groundtruth
             - 2. The BaseEvaluator works as if the `groundtruth` had been provided by the client as it comes in the request.

     One can use the :class:`FileBasedEvaluator` via

     .. highlight:: yaml
     .. code-block:: yaml

         !FileBasedEvaluator
         components:
           - !BinaryPbIndexer
             with:
               index_filename: ground_truth.gz
             metas:
               name: groundtruth_index  # a customized name
               workspace: $TEST_WORKDIR
           - !BaseEvaluator
             metas:
               name: evaluator  # a customized name
         metas:
           name: file_based_evaluator
           workspace: $TEST_WORKDIR

     Without defining any ``requests.on`` logic. When load from this YAML, it will be auto equipped with

     .. highlight:: yaml
     .. code-block:: yaml

         on:
           [SearchRequest, IndexRequest]:
             - !LoadGroundTruthDriver
               with:
                 executor: BaseKVIndexer
             - !BaseEvaluationDriver
               with:
                 executor: BaseEvaluator
           ControlRequest:
             - !ControlReqDriver {}
     """
