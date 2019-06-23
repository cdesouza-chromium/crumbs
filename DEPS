# Copyright (c) 2019 Crumbs Project. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This file is used to manage the dependencies of the Chromium src repo. It is
# used by gclient to determine what version of each dependency to check out, and
# where.
#
# When adding a new dependency, please update the top-level .gitignore file
# to list the dependency's destination directory.
#
# -----------------------------------------------------------------------------
# Rolling deps
# -----------------------------------------------------------------------------
# All repositories in this file are git-based, using Chromium git mirrors where
# necessary (e.g., a git mirror is used when the source project is SVN-based).
# To update the revision that Chromium pulls for a given dependency:
#
#  # Create and switch to a new branch
#  git new-branch depsroll
#  # Run roll-dep (provided by depot_tools) giving the dep's path and optionally
#  # a regex that will match the line in this file that contains the current
#  # revision. The script ALWAYS rolls the dependency to the latest revision
#  # in origin/master. The path for the dep should start with src/.
#  roll-dep src/third_party/foo_package/src foo_package.git
#  # You should now have a modified DEPS file; commit and upload as normal
#  git commit -a
#  git cl upload

gclient_gn_args_file = 'src/build/config/gclient_args.gni'
gclient_gn_args = [
  'build_with_chromium',
]

vars = {
  # Variable that can be used to support multiple build scenarios, like having
  # Chromium specific targets in a client project's GN file or sync dependencies
  # conditionally etc.
  'build_with_chromium': True,

  # By default, we should check out everything needed to run on the main
  # chromium waterfalls. This var can be also be set to "small", in order
  # to skip things are not strictly needed to build chromium for development
  # purposes.
  'checkout_configuration': 'default',

  'checkout_instrumented_libraries': 'checkout_linux and checkout_configuration != "small"',

  # This can be overridden, e.g. with custom_vars, to build clang from HEAD
  # instead of downloading the prebuilt pinned revision.
  'llvm_force_head_revision': False,

  'chromium_git': 'https://chromium.googlesource.com',
  'boringssl_git': 'https://boringssl.googlesource.com',

  # GN CIPD package version.
  'gn_version': 'git_revision:81ee1967d3fcbc829bac1c005c3da59739c88df9',
  
  'chromium_revision': 'HEAD',

  'chromium_build': 'e0e8ea0440416520598e28fbbb4ce3c48c3c1119',
  'chromium_buildtools': '8c2657f8849a3253f387b14bbc095a6214ce05a2',
  'chromium_third_party_jinja2': 'b41863e42637544c2941b574c7877d3e1f663e25',
  'chromium_third_party_markupsafe': '8f45f5cfa0009d2a70589bcda0349b8cb2b72783',
  'chromium_tools_clang': 'fb60bb4436027f860596fdf1db87f7405e34340c',
  'chromium_tools_code_coverage': '279ef3a59e6f0b5ca54415f364b5857359393127',
  'chromium_third_party_depot_tools': '125f7cc4d52d831830561ebfed0d26bfa074003f',

  'chromium_base': 'f156a09292131d3dd003a81179d44fa1061380c4',
  'chromium_testing': '3c824205a2ac3ed2af93e5b21ff733218691fb3b',
  'chromium_third_party_apple_apsl': 'b604130b3e896b095a564726f436d1c45d76f241',
  'chromium_third_party_boringssl': '68a6b39e0f45f819ae79ddcb55d47ccffadbbaa8',
  'chromium_third_party_boringssl_src': '629f321ffd98992febd751526dd1c06eff5f921a',
  'chromium_third_party_ced': 'a2afafea514434c855c38e3cf221ff4358a36caf',
  'chromium_third_party_ced_src': '1193457d7276cd49968f46e98fccc78a27881937',
  'chromium_third_party_depot_tools': 'dd2737e2b5727d836f2442d9a6d960ad978fed66',
  'chromium_third_party_googletest': 'd5024103c8a8977156ee800eb1c84d92dffe9fdf',
  'chromium_third_party_jinja2': 'b41863e42637544c2941b574c7877d3e1f663e25',
  'chromium_third_party_markupsafe': '8f45f5cfa0009d2a70589bcda0349b8cb2b72783',
  'chromium_third_party_modp_b64': '28e3fbba4cb4ec3ffd85b53d0a3904525d08f5a6',
  'chromium_third_party_protobuf': 'c8d45bf67c30b8ded4b1aafe9a9c88bc0c554ffc',
  'chromium_third_party_googletest_src': 'b4676595c03a26bb84f68542c8b74d3d89b38b68',
  'chromium_third_party_icu': 'fd97d4326fac6da84452b2d5fe75ff0949368dab',
  'chromium_third_party_libxml': '3aa9eaae15a878f3a0ddc7dee203267db53248c5',
  'chromium_third_party_zlib': 'db18ea35620e772c9ab2593fb7f08f433c7275c0',
  'chromium_tools_protoc_wrapper': '24f7a690865890c642b452df81c10d3758d2c86f',

 # GN CIPD package version.
  'gn_version': 'git_revision:8c7f49102234f4f4b9349dcb258554675475e596',

  # Also, if you change these, update buildtools/DEPS too. Also update the
  # libc++ svn_revision in //buildtools/deps_revisions.gni.
  'clang_format_revision': 'cd5aff70ee0b0fe27d8cd0a0419e16f628dd688a',
  'libcxx_revision': '20f2ecc8621b57e8fde86c796ccc03d209cd3b1d',
  'libcxxabi_revision': 'c9a6d09e0c2c5bfdf51ed60b6d0335d2d04564f1',
  'libunwind_revision': '563f0d1b04217936a2a903f32dbe0a043eaf549c',
}

# Only these hosts are allowed for dependencies in this DEPS file.
# If you need to add a new host, contact chrome infrastracture team.
allowed_hosts = [
    'chromium.googlesource.com',
    'boringssl.googlesource.com',
]

deps = {
  'src/buildtools/clang_format/script':
    Var('chromium_git') + '/chromium/llvm-project/cfe/tools/clang-format.git@' +
    Var('clang_format_revision'),

  'src/buildtools/linux64': {
    'packages': [
      {
        'package': 'gn/gn/linux-amd64',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "linux"',
  },

  'src/buildtools/mac': {
    'packages': [
      {
        'package': 'gn/gn/mac-amd64',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "mac"',
  },

  'src/buildtools/third_party/libc++/trunk':
    Var('chromium_git') + '/chromium/llvm-project/libcxx.git' + '@' +
    Var('libcxx_revision'),

  'src/buildtools/third_party/libc++abi/trunk':
    Var('chromium_git') + '/chromium/llvm-project/libcxxabi.git' + '@' +
    Var('libcxxabi_revision'),

  'src/buildtools/third_party/libunwind/trunk':
    Var('chromium_git') + '/external/llvm.org/libunwind.git' + '@' +
    Var('libunwind_revision'),

  'src/buildtools/win': {
    'packages': [
      {
        'package': 'gn/gn/windows-amd64',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "win"',
  },

  'src/build':
    Var('chromium_git') + '/chromium/src/build' + '@' + Var('chromium_build'),

  'src/buildtools':
    Var('chromium_git') + '/chromium/src/buildtools' + '@' + Var('chromium_buildtools'),

  'src/third_party/jinja2':
    Var('chromium_git') + '/chromium/src/third_party/jinja2' + '@' + Var('chromium_third_party_jinja2'),

  'src/third_party/markupsafe':
    Var('chromium_git') + '/chromium/src/third_party/markupsafe' + '@' + Var('chromium_third_party_markupsafe'),

  'src/tools/clang':
    Var('chromium_git') + '/chromium/src/tools/clang' + '@' + Var('chromium_tools_clang'),

  'src/tools/code_coverage':
    Var('chromium_git') + '/chromium/src/tools/code_coverage' + '@' + Var('chromium_tools_code_coverage'),

  'src/third_party/depot_tools':
    Var('chromium_git') + '/chromium/tools/depot_tools.git' + '@' + Var('chromium_third_party_depot_tools'),

  #base deps from this point onwards
  'src/base':
    Var('chromium_git') + '/chromium/src/base' + '@' + Var('chromium_base'),

  'src/testing':
    Var('chromium_git') + '/chromium/src/testing' + '@' + Var('chromium_testing'),

  'src/third_party/apple_apsl':
    Var('chromium_git') + '/chromium/src/third_party/apple_apsl' + '@' + Var('chromium_third_party_apple_apsl'),

  'src/third_party/boringssl':
    Var('chromium_git') + '/chromium/src/third_party/boringssl' + '@' + Var('chromium_third_party_boringssl'),

  'src/third_party/boringssl/src':
    Var('boringssl_git') + '/boringssl.git' + '@' +  Var('chromium_third_party_boringssl_src'),

  'src/third_party/ced':
    Var('chromium_git') + '/chromium/src/third_party/ced' + '@' + Var('chromium_third_party_ced'),

  'src/third_party/ced/src':
    Var('chromium_git') + '/external/github.com/google/compact_enc_det.git' + '@' + Var('chromium_third_party_ced_src'),

  'src/third_party/depot_tools':
    Var('chromium_git') + '/chromium/tools/depot_tools.git' + '@' + Var('chromium_third_party_depot_tools'),

  'src/third_party/googletest':
    Var('chromium_git') + '/chromium/src/third_party/googletest' + '@' + Var('chromium_third_party_googletest'),

  'src/third_party/jinja2':
    Var('chromium_git') + '/chromium/src/third_party/jinja2' + '@' + Var('chromium_third_party_jinja2'),

  'src/third_party/markupsafe':
    Var('chromium_git') + '/chromium/src/third_party/markupsafe' + '@' + Var('chromium_third_party_markupsafe'),

  'src/third_party/modp_b64':
    Var('chromium_git') + '/chromium/src/third_party/modp_b64' + '@' + Var('chromium_third_party_modp_b64'),

  'src/third_party/protobuf':
    Var('chromium_git') + '/chromium/src/third_party/protobuf' + '@' + Var('chromium_third_party_protobuf'),

  'src/third_party/googletest/src':
    Var('chromium_git') + '/external/github.com/google/googletest.git' + '@' + Var('chromium_third_party_googletest_src'),

  'src/third_party/icu':
    Var('chromium_git') + '/chromium/deps/icu.git' + '@' + Var('chromium_third_party_icu'),

  'src/third_party/libxml':
    Var('chromium_git') + '/chromium/src/third_party/libxml' + '@' + Var('chromium_third_party_libxml'),

  'src/third_party/zlib':
    Var('chromium_git') + '/chromium/src/third_party/zlib' + '@' + Var('chromium_third_party_zlib'),

  'src/tools/protoc_wrapper':
    Var('chromium_git') + '/chromium/src/tools/protoc_wrapper' + '@' + Var('chromium_tools_protoc_wrapper'),
}

hooks = [
  {
    # This clobbers when necessary (based on get_landmines.py). It must be the
    # first hook so that other things that get/generate into the output
    # directory will not subsequently be clobbered.
    'name': 'landmines',
    'pattern': '.',
    'action': [
        'python',
        'src/build/landmines.py',
    ],
  },
  {
    # Ensure that the DEPS'd "depot_tools" has its self-update capability
    # disabled.
    'name': 'disable_depot_tools_selfupdate',
    'pattern': '.',
    'action': [
        'python',
        'src/third_party/depot_tools/update_depot_tools_toggle.py',
        '--disable',
    ],
  },
  {
    # Ensure that we don't accidentally reference any .pyc files whose
    # corresponding .py files have since been deleted.
    # We could actually try to avoid generating .pyc files, crbug.com/500078.
    'name': 'remove_stale_pyc_files',
    'pattern': '.',
    'action': [
        'python',
        'src/tools/remove_stale_pyc_files.py',
        'src/tools',
    ],
  },
  {
    # Verify that we have the right GN binary and force-install it if we
    # don't, in order to work around crbug.com/944367.
    # TODO(crbug.com/944667) Get rid of this when cipd is ensuring we
    # have the right binary more carefully and we no longer need this.
    'name': 'ensure_gn_version',
    'pattern': '.',
    'action': [
      'python',
      'src/buildtools/ensure_gn_version.py',
      Var('gn_version')
    ],
  },
  {
    'name': 'sysroot_arm',
    'pattern': '.',
    'condition': 'checkout_linux and checkout_arm',
    'action': ['python', 'src/build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=arm'],
  },
  {
    'name': 'sysroot_arm64',
    'pattern': '.',
    'condition': 'checkout_linux and checkout_arm64',
    'action': ['python', 'src/build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=arm64'],
  },
  {
    'name': 'sysroot_x86',
    'pattern': '.',
    'condition': 'checkout_linux and (checkout_x86 or checkout_x64)',
    'action': ['python', 'src/build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=x86'],
  },
  {
    'name': 'sysroot_mips',
    'pattern': '.',
    'condition': 'checkout_linux and checkout_mips',
    'action': ['python', 'src/build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=mips'],
  },
  {
    'name': 'sysroot_mips64',
    'pattern': '.',
    'condition': 'checkout_linux and checkout_mips64',
    'action': ['python', 'src/build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=mips64el'],
  },

  {
    'name': 'sysroot_x64',
    'pattern': '.',
    'condition': 'checkout_linux and checkout_x64',
    'action': ['python', 'src/build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=x64'],
  },
  {
    # Case-insensitivity for the Win SDK. Must run before win_toolchain below.
    'name': 'ciopfs_linux',
    'pattern': '.',
    'condition': 'checkout_win and host_os == "linux"',
    'action': [ 'python',
                'src/third_party/depot_tools/download_from_google_storage.py',
                '--no_resume',
                '--no_auth',
                '--bucket', 'chromium-browser-clang/ciopfs',
                '-s', 'src/build/ciopfs.sha1',
    ]
  },
  {
    # Update the Windows toolchain if necessary.  Must run before 'clang' below.
    'name': 'win_toolchain',
    'pattern': '.',
    'condition': 'checkout_win',
    'action': ['python', 'src/build/vs_toolchain.py', 'update', '--force'],
  },
  {
    # Update the Mac toolchain if necessary.
    'name': 'mac_toolchain',
    'pattern': '.',
    'condition': 'checkout_ios or checkout_mac',
    'action': ['python', 'src/build/mac_toolchain.py'],
  },
  # Pull binutils for linux, enabled debug fission for faster linking /
  # debugging when used with clang on Ubuntu Precise.
  # https://code.google.com/p/chromium/issues/detail?id=352046
  {
    'name': 'binutils',
    'pattern': 'src/third_party/binutils',
    'condition': 'host_os == "linux" and host_cpu != "mips64"',
    'action': [
        'python',
        'src/third_party/binutils/download.py',
    ],
  },
  {
    # Update the prebuilt clang toolchain.
    # Note: On Win, this should run after win_toolchain, as it may use it.
    'name': 'clang',
    'pattern': '.',
    'condition': 'not llvm_force_head_revision',
    'action': ['python', 'src/tools/clang/scripts/update.py'],
  },
  {
    # Build the clang toolchain from tip-of-tree.
    # Note: On Win, this should run after win_toolchain, as it may use it.
    'name': 'clang_tot',
    'pattern': '.',
    'condition': 'llvm_force_head_revision',
    'action': ['python', 'src/tools/clang/scripts/build.py',
               '--llvm-force-head-revision',
               '--with-android={checkout_android}'],
  },
  {
    # This is supposed to support the same set of platforms as 'clang' above.
    'name': 'clang_coverage',
    'pattern': '.',
    'condition': 'checkout_clang_coverage_tools',
    'action': ['python', 'src/tools/code_coverage/update_clang_coverage_tools.py'],
  },
  {
    # Mac doesn't use lld so it's not included in the default clang bundle
    # there.  lld is however needed in win and Fuchsia cross builds, so
    # download it there. Should run after the clang hook.
    'name': 'lld/mac',
    'pattern': '.',
    'condition': 'host_os == "mac" and (checkout_win or checkout_fuchsia)',
    'action': ['python', 'src/tools/clang/scripts/download_lld_mac.py'],
  },
  {
    # Update LASTCHANGE.
    'name': 'lastchange',
    'pattern': '.',
    'action': ['python', 'src/build/util/lastchange.py',
               '-o', 'src/build/util/LASTCHANGE'],
  },
  # Pull clang-format binaries using checked-in hashes.
  {
    'name': 'clang_format_win',
    'pattern': '.',
    'condition': 'host_os == "win"',
    'action': [ 'python',
                'src/third_party/depot_tools/download_from_google_storage.py',
                '--no_resume',
                '--no_auth',
                '--bucket', 'chromium-clang-format',
                '-s', 'src/buildtools/win/clang-format.exe.sha1',
    ],
  },
  {
    'name': 'clang_format_mac',
    'pattern': '.',
    'condition': 'host_os == "mac"',
    'action': [ 'python',
                'src/third_party/depot_tools/download_from_google_storage.py',
                '--no_resume',
                '--no_auth',
                '--bucket', 'chromium-clang-format',
                '-s', 'src/buildtools/mac/clang-format.sha1',
    ],
  },
  {
    'name': 'clang_format_linux',
    'pattern': '.',
    'condition': 'host_os == "linux"',
    'action': [ 'python',
                'src/third_party/depot_tools/download_from_google_storage.py',
                '--no_resume',
                '--no_auth',
                '--bucket', 'chromium-clang-format',
                '-s', 'src/buildtools/linux64/clang-format.sha1',
    ],
  },
  {
    'name': 'msan_chained_origins',
    'pattern': '.',
    'condition': 'checkout_instrumented_libraries',
    'action': [ 'python',
                'src/third_party/depot_tools/download_from_google_storage.py',
                '--no_resume',
                '--no_auth',
                '--bucket', 'chromium-instrumented-libraries',
                '-s', 'src/third_party/instrumented_libraries/binaries/msan-chained-origins-trusty.tgz.sha1',
              ],
  },
  {
    'name': 'msan_no_origins',
    'pattern': '.',
    'condition': 'checkout_instrumented_libraries',
    'action': [ 'python',
                'src/third_party/depot_tools/download_from_google_storage.py',
                '--no_resume',
                '--no_auth',
                '--bucket', 'chromium-instrumented-libraries',
                '-s', 'src/third_party/instrumented_libraries/binaries/msan-no-origins-trusty.tgz.sha1',
              ],
  },
  {
    'name': 'fuchsia_sdk',
    'pattern': '.',
    'condition': 'checkout_fuchsia',
    'action': [
      'python',
      'src/build/fuchsia/update_sdk.py',
    ],
  },
]
