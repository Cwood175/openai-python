from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._events import (
        ResponseTextDoneEvent as ResponseTextDoneEvent,
        ResponseTextDeltaEvent as ResponseTextDeltaEvent,
        ResponseFunctionCallArgumentsDeltaEvent as ResponseFunctionCallArgumentsDeltaEvent,
    )
else:
    # Defer importing _events at runtime to avoid import-time side effects
    try:
        from ._events import (
            ResponseTextDoneEvent as ResponseTextDoneEvent,
            ResponseTextDeltaEvent as ResponseTextDeltaEvent,
            ResponseFunctionCallArgumentsDeltaEvent as ResponseFunctionCallArgumentsDeltaEvent,
        )
    except Exception:
        # In environments where _events' dependencies aren't available at import time,
        # provide fallbacks to avoid failing module import. Type checkers will still
        # see the actual types because of TYPE_CHECKING above.
        ResponseTextDoneEvent = None  # type: ignore
        ResponseTextDeltaEvent = None  # type: ignore
        ResponseFunctionCallArgumentsDeltaEvent = None  # type: ignore

from ._responses import (
    ResponseStream as ResponseStream,
    AsyncResponseStream as AsyncResponseStream,
    ResponseStreamEvent as ResponseStreamEvent,
    ResponseStreamState as ResponseStreamState,
    ResponseStreamManager as ResponseStreamManager,
    AsyncResponseStreamManager as AsyncResponseStreamManager,
)
