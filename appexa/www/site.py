"""Serves the built appexa-frontend SPA.

Vite writes hashed filenames, so the template reads the asset names out of the
build manifest rather than hardcoding them. Falls back to no assets, and the
template then explains how to build.
"""

import json
import os

import frappe

no_cache = 1

BUILD_DIR = "public/frontend"
ASSET_BASE = "/assets/appexa/frontend"


def _manifest_paths():
	manifest_path = os.path.join(
		frappe.get_app_path("appexa"), BUILD_DIR, ".vite", "manifest.json"
	)
	if not os.path.exists(manifest_path):
		return [], []

	with open(manifest_path) as handle:
		manifest = json.load(handle)

	entry = next((chunk for chunk in manifest.values() if chunk.get("isEntry")), None)
	if not entry:
		return [], []

	js = [f"{ASSET_BASE}/{entry['file']}"]
	css = [f"{ASSET_BASE}/{path}" for path in entry.get("css", [])]
	return js, css


def get_context(context):
	context.frontend_js, context.frontend_css = _manifest_paths()
	context.no_breadcrumbs = True
	return context
