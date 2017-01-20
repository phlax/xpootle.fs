# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from pootle.core.plugin import provider
from pootle_fs.delegate import fs_plugins, fs_upstream

from .plugin import GitPlugin
from .upstream import GithubUpstreamFS


@provider(fs_plugins)
def git_plugin_provider(**kwargs):
    return dict(git=GitPlugin)


@provider(fs_upstream)
def github_upstream_provider(**kwargs):
    return dict(github=GithubUpstreamFS)
