from __future__ import annotations

from openclaw_erp.demo import build_nig_commerce_context


def get_context(context):
	for key, value in build_nig_commerce_context().items():
		setattr(context, key, value)
	context.show_sidebar = False
	context.no_breadcrumbs = True
