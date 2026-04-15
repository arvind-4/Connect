"""Views for the video chat room."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from backend.video.utils import create_unique_uuid

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@login_required
def new_meet_view(*_args: tuple[Any, ...], **_kwargs: dict[str, Any]) -> HttpResponse:
    """Create a new video chat room."""
    room_id = create_unique_uuid()
    redirect_url = f"/{room_id}"
    return redirect(redirect_url)


@login_required
def meet_view(request: HttpRequest, room_id: str | None = None) -> HttpResponse:
    """Render the main view for the video chat room."""
    context = {"room_id": room_id}
    return render(request, "video/index.html", context=context)
