<div id="geany" class="document">

# Geany

## A fast, light, GTK+ IDE

<table class="docinfo" data-frame="void" data-rules="none">
<tbody data-valign="top">
<tr class="odd">
<th class="docinfo-name">Authors:</th>
<td>Enrico Tröger<br />
Nick Treleaven<br />
Frank Lanitz<br />
Colomban Wendling<br />
Matthew Brush</td>
</tr>
<tr class="even">
<th class="docinfo-name">Date:</th>
<td>2025-07-06</td>
</tr>
<tr class="odd">
<th class="docinfo-name">Version:</th>
<td>2.1</td>
</tr>
</tbody>
</table>

Copyright © 2005 The Geany contributors

This document is distributed under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. A copy of this license can be found in the file COPYING included with the source code of this program, and also in the chapter <a href="#gnu-general-public-license" class="reference internal">GNU General Public License</a>.

<div id="contents" class="contents topic">

Contents

-   <a href="#introduction" id="toc-entry-1" class="reference internal">Introduction</a>
    -   <a href="#about-geany" id="toc-entry-2" class="reference internal">About Geany</a>
    -   <a href="#where-to-get-it" id="toc-entry-3" class="reference internal">Where to get it</a>
    -   <a href="#license" id="toc-entry-4" class="reference internal">License</a>
    -   <a href="#about-this-document" id="toc-entry-5" class="reference internal">About this document</a>
-   <a href="#installation" id="toc-entry-6" class="reference internal">Installation</a>
    -   <a href="#requirements" id="toc-entry-7" class="reference internal">Requirements</a>
    -   <a href="#binary-packages" id="toc-entry-8" class="reference internal">Binary packages</a>
    -   <a href="#source-compilation" id="toc-entry-9" class="reference internal">Source compilation</a>
        -   <a href="#autotools-based-build-system" id="toc-entry-10" class="reference internal">Autotools based build system</a>
        -   <a href="#custom-installation" id="toc-entry-11" class="reference internal">Custom installation</a>
        -   <a href="#dynamic-linking-loader-support-and-vte" id="toc-entry-12" class="reference internal">Dynamic linking loader support and VTE</a>
        -   <a href="#build-problems" id="toc-entry-13" class="reference internal">Build problems</a>
    -   <a href="#installation-prefix" id="toc-entry-14" class="reference internal">Installation prefix</a>
-   <a href="#usage" id="toc-entry-15" class="reference internal">Usage</a>
    -   <a href="#getting-started" id="toc-entry-16" class="reference internal">Getting started</a>
    -   <a href="#the-geany-workspace" id="toc-entry-17" class="reference internal">The Geany workspace</a>
        -   <a href="#sidebar-usage" id="toc-entry-18" class="reference internal">Sidebar Usage</a>
    -   <a href="#command-line-options" id="toc-entry-19" class="reference internal">Command line options</a>
    -   <a href="#general" id="toc-entry-20" class="reference internal">General</a>
        -   <a href="#startup" id="toc-entry-21" class="reference internal">Startup</a>
        -   <a href="#opening-files" id="toc-entry-22" class="reference internal">Opening files</a>
            -   <a href="#open-dialog" id="toc-entry-23" class="reference internal">Open dialog</a>
            -   <a href="#opening-files-from-the-command-line-in-a-running-instance" id="toc-entry-24" class="reference internal">Opening files from the command-line in a running instance</a>
        -   <a href="#virtual-terminal-emulator-widget-vte" id="toc-entry-25" class="reference internal">Virtual terminal emulator widget (VTE)</a>
    -   <a href="#documents" id="toc-entry-26" class="reference internal">Documents</a>
        -   <a href="#switching-between-documents" id="toc-entry-27" class="reference internal">Switching between documents</a>
        -   <a href="#document-list-views" id="toc-entry-28" class="reference internal">Document list views</a>
        -   <a href="#cloning-documents" id="toc-entry-29" class="reference internal">Cloning documents</a>
        -   <a href="#automatic-filename-insertion-on-save-as" id="toc-entry-30" class="reference internal">Automatic filename insertion on Save As...</a>
    -   <a href="#character-sets-and-unicode-byte-order-mark-bom" id="toc-entry-31" class="reference internal">Character sets and Unicode Byte-Order-Mark (BOM)</a>
        -   <a href="#using-character-sets" id="toc-entry-32" class="reference internal">Using character sets</a>
        -   <a href="#in-file-encoding-specification" id="toc-entry-33" class="reference internal">In-file encoding specification</a>
        -   <a href="#special-encoding-none" id="toc-entry-34" class="reference internal">Special encoding "None"</a>
        -   <a href="#unicode-byte-order-mark-bom" id="toc-entry-35" class="reference internal">Unicode Byte-Order-Mark (BOM)</a>
    -   <a href="#editing" id="toc-entry-36" class="reference internal">Editing</a>
        -   <a href="#folding" id="toc-entry-37" class="reference internal">Folding</a>
        -   <a href="#column-mode-editing-rectangular-selections" id="toc-entry-38" class="reference internal">Column mode editing (rectangular selections)</a>
        -   <a href="#drag-and-drop-of-text" id="toc-entry-39" class="reference internal">Drag and drop of text</a>
        -   <a href="#indentation" id="toc-entry-40" class="reference internal">Indentation</a>
            -   <a href="#applying-new-indentation-settings" id="toc-entry-41" class="reference internal">Applying new indentation settings</a>
            -   <a href="#detecting-indent-type" id="toc-entry-42" class="reference internal">Detecting indent type</a>
        -   <a href="#auto-indentation" id="toc-entry-43" class="reference internal">Auto-indentation</a>
        -   <a href="#bookmarks" id="toc-entry-44" class="reference internal">Bookmarks</a>
        -   <a href="#code-navigation-history" id="toc-entry-45" class="reference internal">Code navigation history</a>
        -   <a href="#sending-text-through-custom-commands" id="toc-entry-46" class="reference internal">Sending text through custom commands</a>
        -   <a href="#context-actions" id="toc-entry-47" class="reference internal">Context actions</a>
        -   <a href="#autocompletion" id="toc-entry-48" class="reference internal">Autocompletion</a>
            -   <a href="#word-part-completion" id="toc-entry-49" class="reference internal">Word part completion</a>
            -   <a href="#scope-autocompletion" id="toc-entry-50" class="reference internal">Scope autocompletion</a>
        -   <a href="#calltips" id="toc-entry-51" class="reference internal">Calltips</a>
        -   <a href="#user-definable-snippets" id="toc-entry-52" class="reference internal">User-definable snippets</a>
            -   <a href="#snippet-keybindings" id="toc-entry-53" class="reference internal">Snippet keybindings</a>
        -   <a href="#inserting-unicode-characters" id="toc-entry-54" class="reference internal">Inserting Unicode characters</a>
        -   <a href="#inserting-color-values" id="toc-entry-55" class="reference internal">Inserting color values</a>
    -   <a href="#search-replace-and-go-to" id="toc-entry-56" class="reference internal">Search, replace and go to</a>
        -   <a href="#toolbar-entries" id="toc-entry-57" class="reference internal">Toolbar entries</a>
            -   <a href="#search-bar" id="toc-entry-58" class="reference internal">Search bar</a>
        -   <a href="#find" id="toc-entry-59" class="reference internal">Find</a>
            -   <a href="#matching-options" id="toc-entry-60" class="reference internal">Matching options</a>
            -   <a href="#find-all" id="toc-entry-61" class="reference internal">Find all</a>
            -   <a href="#change-font-in-search-dialog-text-fields" id="toc-entry-62" class="reference internal">Change font in search dialog text fields</a>
        -   <a href="#find-selection" id="toc-entry-63" class="reference internal">Find selection</a>
        -   <a href="#find-usage" id="toc-entry-64" class="reference internal">Find usage</a>
        -   <a href="#find-in-files" id="toc-entry-65" class="reference internal">Find in files</a>
            -   <a href="#filtering-out-version-control-files" id="toc-entry-66" class="reference internal">Filtering out version control files</a>
        -   <a href="#replace" id="toc-entry-67" class="reference internal">Replace</a>
            -   <a href="#replace-all" id="toc-entry-68" class="reference internal">Replace all</a>
        -   <a href="#go-to-symbol-definition" id="toc-entry-69" class="reference internal">Go to symbol definition</a>
        -   <a href="#go-to-symbol-declaration" id="toc-entry-70" class="reference internal">Go to symbol declaration</a>
        -   <a href="#go-to-line" id="toc-entry-71" class="reference internal">Go to line</a>
        -   <a href="#regular-expressions" id="toc-entry-72" class="reference internal">Regular expressions</a>
            -   <a href="#multi-line-regular-expressions" id="toc-entry-73" class="reference internal">Multi-line regular expressions</a>
    -   <a href="#view-menu" id="toc-entry-74" class="reference internal">View menu</a>
        -   <a href="#color-schemes-dialog" id="toc-entry-75" class="reference internal">Color schemes dialog</a>
    -   <a href="#symbols-and-tags-files" id="toc-entry-76" class="reference internal">Symbols and tags files</a>
        -   <a href="#workspace-symbols" id="toc-entry-77" class="reference internal">Workspace symbols</a>
        -   <a href="#global-tags-files" id="toc-entry-78" class="reference internal">Global tags files</a>
            -   <a href="#default-global-tags-files" id="toc-entry-79" class="reference internal">Default global tags files</a>
            -   <a href="#global-tags-file-format" id="toc-entry-80" class="reference internal">Global tags file format</a>
                -   <a href="#ctags-format" id="toc-entry-81" class="reference internal">CTags format</a>
                -   <a href="#pipe-separated-format" id="toc-entry-82" class="reference internal">Pipe-separated format</a>
                -   <a href="#tagmanager-format" id="toc-entry-83" class="reference internal">Tagmanager format</a>
            -   <a href="#generating-a-global-tags-file" id="toc-entry-84" class="reference internal">Generating a global tags file</a>
                -   <a href="#generating-tags-files-using-ctags" id="toc-entry-85" class="reference internal">Generating tags files using ctags</a>
                -   <a href="#generating-tags-files-using-geany" id="toc-entry-86" class="reference internal">Generating tags files using Geany</a>
                -   <a href="#generating-c-c-tags-files-using-geany" id="toc-entry-87" class="reference internal">Generating C/C++ tags files using Geany</a>
                -   <a href="#generating-tags-files-on-windows-using-geany" id="toc-entry-88" class="reference internal">Generating tags files on Windows using Geany</a>
        -   <a href="#c-ignore-tags" id="toc-entry-89" class="reference internal">C ignore.tags</a>
    -   <a href="#preferences" id="toc-entry-90" class="reference internal">Preferences</a>
        -   <a href="#general-startup-preferences" id="toc-entry-91" class="reference internal">General Startup preferences</a>
            -   <a href="#startup-1" id="toc-entry-92" class="reference internal">Startup</a>
            -   <a href="#shutdown" id="toc-entry-93" class="reference internal">Shutdown</a>
            -   <a href="#paths" id="toc-entry-94" class="reference internal">Paths</a>
        -   <a href="#general-miscellaneous-preferences" id="toc-entry-95" class="reference internal">General Miscellaneous preferences</a>
            -   <a href="#miscellaneous" id="toc-entry-96" class="reference internal">Miscellaneous</a>
            -   <a href="#search" id="toc-entry-97" class="reference internal">Search</a>
            -   <a href="#projects" id="toc-entry-98" class="reference internal">Projects</a>
        -   <a href="#interface-preferences" id="toc-entry-99" class="reference internal">Interface preferences</a>
            -   <a href="#sidebar" id="toc-entry-100" class="reference internal">Sidebar</a>
            -   <a href="#message-window" id="toc-entry-101" class="reference internal">Message window</a>
            -   <a href="#fonts" id="toc-entry-102" class="reference internal">Fonts</a>
            -   <a href="#miscellaneous-1" id="toc-entry-103" class="reference internal">Miscellaneous</a>
        -   <a href="#interface-notebook-tab-preferences" id="toc-entry-104" class="reference internal">Interface Notebook tab preferences</a>
            -   <a href="#editor-tabs" id="toc-entry-105" class="reference internal">Editor tabs</a>
            -   <a href="#tab-positions" id="toc-entry-106" class="reference internal">Tab positions</a>
        -   <a href="#interface-toolbar-preferences" id="toc-entry-107" class="reference internal">Interface Toolbar preferences</a>
            -   <a href="#toolbar" id="toc-entry-108" class="reference internal">Toolbar</a>
            -   <a href="#appearance" id="toc-entry-109" class="reference internal">Appearance</a>
        -   <a href="#editor-features-preferences" id="toc-entry-110" class="reference internal">Editor Features preferences</a>
            -   <a href="#features" id="toc-entry-111" class="reference internal">Features</a>
        -   <a href="#editor-indentation-preferences" id="toc-entry-112" class="reference internal">Editor Indentation preferences</a>
            -   <a href="#indentation-group" id="toc-entry-113" class="reference internal">Indentation group</a>
        -   <a href="#editor-completions-preferences" id="toc-entry-114" class="reference internal">Editor Completions preferences</a>
            -   <a href="#completions" id="toc-entry-115" class="reference internal">Completions</a>
            -   <a href="#auto-close-quotes-and-brackets" id="toc-entry-116" class="reference internal">Auto-close quotes and brackets</a>
        -   <a href="#editor-display-preferences" id="toc-entry-117" class="reference internal">Editor Display preferences</a>
            -   <a href="#display" id="toc-entry-118" class="reference internal">Display</a>
            -   <a href="#long-line-marker" id="toc-entry-119" class="reference internal">Long line marker</a>
            -   <a href="#virtual-spaces" id="toc-entry-120" class="reference internal">Virtual spaces</a>
            -   <a href="#change-history" id="toc-entry-121" class="reference internal">Change History</a>
        -   <a href="#files-preferences" id="toc-entry-122" class="reference internal">Files preferences</a>
            -   <a href="#new-files" id="toc-entry-123" class="reference internal">New files</a>
            -   <a href="#saving-files" id="toc-entry-124" class="reference internal">Saving files</a>
            -   <a href="#miscellaneous-2" id="toc-entry-125" class="reference internal">Miscellaneous</a>
        -   <a href="#tools-preferences" id="toc-entry-126" class="reference internal">Tools preferences</a>
            -   <a href="#tool-paths" id="toc-entry-127" class="reference internal">Tool paths</a>
            -   <a href="#commands" id="toc-entry-128" class="reference internal">Commands</a>
        -   <a href="#template-preferences" id="toc-entry-129" class="reference internal">Template preferences</a>
            -   <a href="#template-data" id="toc-entry-130" class="reference internal">Template data</a>
        -   <a href="#keybinding-preferences" id="toc-entry-131" class="reference internal">Keybinding preferences</a>
        -   <a href="#printing-preferences" id="toc-entry-132" class="reference internal">Printing preferences</a>
        -   <a href="#various-preferences" id="toc-entry-133" class="reference internal">Various preferences</a>
            -   <a href="#statusbar-templates" id="toc-entry-134" class="reference internal">Statusbar Templates</a>
        -   <a href="#terminal-vte-preferences" id="toc-entry-135" class="reference internal">Terminal (VTE) preferences</a>
            -   <a href="#terminal-widget" id="toc-entry-136" class="reference internal">Terminal widget</a>
    -   <a href="#project-management" id="toc-entry-137" class="reference internal">Project management</a>
        -   <a href="#new-project" id="toc-entry-138" class="reference internal">New project</a>
        -   <a href="#project-properties" id="toc-entry-139" class="reference internal">Project properties</a>
        -   <a href="#open-project" id="toc-entry-140" class="reference internal">Open project</a>
        -   <a href="#close-project" id="toc-entry-141" class="reference internal">Close project</a>
    -   <a href="#build-menu" id="toc-entry-142" class="reference internal">Build menu</a>
        -   <a href="#indicators" id="toc-entry-143" class="reference internal">Indicators</a>
        -   <a href="#default-build-menu-items" id="toc-entry-144" class="reference internal">Default build menu items</a>
            -   <a href="#compile" id="toc-entry-145" class="reference internal">Compile</a>
            -   <a href="#build" id="toc-entry-146" class="reference internal">Build</a>
            -   <a href="#lint" id="toc-entry-147" class="reference internal">Lint</a>
            -   <a href="#make" id="toc-entry-148" class="reference internal">Make</a>
            -   <a href="#make-custom-target" id="toc-entry-149" class="reference internal">Make custom target</a>
            -   <a href="#make-object" id="toc-entry-150" class="reference internal">Make object</a>
            -   <a href="#next-error" id="toc-entry-151" class="reference internal">Next error</a>
            -   <a href="#previous-error" id="toc-entry-152" class="reference internal">Previous error</a>
            -   <a href="#execute" id="toc-entry-153" class="reference internal">Execute</a>
            -   <a href="#stopping-running-processes" id="toc-entry-154" class="reference internal">Stopping running processes</a>
                -   <a href="#terminal-emulators" id="toc-entry-155" class="reference internal">Terminal emulators</a>
            -   <a href="#set-build-commands" id="toc-entry-156" class="reference internal">Set build commands</a>
        -   <a href="#build-menu-configuration" id="toc-entry-157" class="reference internal">Build menu configuration</a>
        -   <a href="#set-build-commands-dialog" id="toc-entry-158" class="reference internal">Set Build Commands dialog</a>
            -   <a href="#substitutions-in-commands-and-working-directories" id="toc-entry-159" class="reference internal">Substitutions in commands and working directories</a>
            -   <a href="#build-menu-keyboard-shortcuts" id="toc-entry-160" class="reference internal">Build menu keyboard shortcuts</a>
            -   <a href="#old-settings" id="toc-entry-161" class="reference internal">Old settings</a>
    -   <a href="#printing-support" id="toc-entry-162" class="reference internal">Printing support</a>
    -   <a href="#plugins" id="toc-entry-163" class="reference internal">Plugins</a>
        -   <a href="#plugin-manager" id="toc-entry-164" class="reference internal">Plugin manager</a>
    -   <a href="#keybindings" id="toc-entry-165" class="reference internal">Keybindings</a>
        -   <a href="#switching-documents" id="toc-entry-166" class="reference internal">Switching documents</a>
        -   <a href="#configurable-keybindings" id="toc-entry-167" class="reference internal">Configurable keybindings</a>
            -   <a href="#file-keybindings" id="toc-entry-168" class="reference internal">File keybindings</a>
            -   <a href="#editor-keybindings" id="toc-entry-169" class="reference internal">Editor keybindings</a>
            -   <a href="#clipboard-keybindings" id="toc-entry-170" class="reference internal">Clipboard keybindings</a>
            -   <a href="#select-keybindings" id="toc-entry-171" class="reference internal">Select keybindings</a>
            -   <a href="#insert-keybindings" id="toc-entry-172" class="reference internal">Insert keybindings</a>
            -   <a href="#format-keybindings" id="toc-entry-173" class="reference internal">Format keybindings</a>
            -   <a href="#settings-keybindings" id="toc-entry-174" class="reference internal">Settings keybindings</a>
            -   <a href="#search-keybindings" id="toc-entry-175" class="reference internal">Search keybindings</a>
            -   <a href="#go-to-keybindings" id="toc-entry-176" class="reference internal">Go to keybindings</a>
            -   <a href="#view-keybindings" id="toc-entry-177" class="reference internal">View keybindings</a>
            -   <a href="#focus-keybindings" id="toc-entry-178" class="reference internal">Focus keybindings</a>
            -   <a href="#notebook-tab-keybindings" id="toc-entry-179" class="reference internal">Notebook tab keybindings</a>
            -   <a href="#document-keybindings" id="toc-entry-180" class="reference internal">Document keybindings</a>
            -   <a href="#project-keybindings" id="toc-entry-181" class="reference internal">Project keybindings</a>
            -   <a href="#build-keybindings" id="toc-entry-182" class="reference internal">Build keybindings</a>
            -   <a href="#tools-keybindings" id="toc-entry-183" class="reference internal">Tools keybindings</a>
            -   <a href="#help-keybindings" id="toc-entry-184" class="reference internal">Help keybindings</a>
-   <a href="#configuration-files" id="toc-entry-185" class="reference internal">Configuration files</a>
    -   <a href="#configuration-file-paths" id="toc-entry-186" class="reference internal">Configuration file paths</a>
        -   <a href="#paths-on-unix-like-systems" id="toc-entry-187" class="reference internal">Paths on Unix-like systems</a>
        -   <a href="#paths-on-windows" id="toc-entry-188" class="reference internal">Paths on Windows</a>
    -   <a href="#tools-menu-items" id="toc-entry-189" class="reference internal">Tools menu items</a>
        -   <a href="#customizing-geany-s-appearance-using-gtk-css" id="toc-entry-190" class="reference internal">Customizing Geany's appearance using GTK+ CSS</a>
    -   <a href="#global-configuration-file" id="toc-entry-191" class="reference internal">Global configuration file</a>
    -   <a href="#filetype-definition-files" id="toc-entry-192" class="reference internal">Filetype definition files</a>
        -   <a href="#filenames" id="toc-entry-193" class="reference internal">Filenames</a>
        -   <a href="#system-files" id="toc-entry-194" class="reference internal">System files</a>
        -   <a href="#user-files" id="toc-entry-195" class="reference internal">User files</a>
        -   <a href="#custom-filetypes" id="toc-entry-196" class="reference internal">Custom filetypes</a>
            -   <a href="#creating-a-custom-filetype-from-an-existing-filetype" id="toc-entry-197" class="reference internal">Creating a custom filetype from an existing filetype</a>
        -   <a href="#filetype-configuration" id="toc-entry-198" class="reference internal">Filetype configuration</a>
            -   <a href="#styling-section" id="toc-entry-199" class="reference internal">[styling] section</a>
                -   <a href="#using-a-named-style" id="toc-entry-200" class="reference internal">Using a named style</a>
                -   <a href="#reading-styles-from-another-filetype" id="toc-entry-201" class="reference internal">Reading styles from another filetype</a>
            -   <a href="#keywords-section" id="toc-entry-202" class="reference internal">[keywords] section</a>
            -   <a href="#lexer-properties-section" id="toc-entry-203" class="reference internal">[lexer_properties] section</a>
            -   <a href="#settings-section" id="toc-entry-204" class="reference internal">[settings] section</a>
            -   <a href="#indentation-section" id="toc-entry-205" class="reference internal">[indentation] section</a>
            -   <a href="#build-menu-filetype-section" id="toc-entry-206" class="reference internal">[build-menu] filetype section</a>
            -   <a href="#build-settings-section" id="toc-entry-207" class="reference internal">[build_settings] section</a>
        -   <a href="#special-file-filetypes-common" id="toc-entry-208" class="reference internal">Special file filetypes.common</a>
            -   <a href="#named-styles-section" id="toc-entry-209" class="reference internal">[named_styles] section</a>
            -   <a href="#named-colors-section" id="toc-entry-210" class="reference internal">[named_colors] section</a>
            -   <a href="#styling-section-1" id="toc-entry-211" class="reference internal">[styling] section</a>
            -   <a href="#settings-section-1" id="toc-entry-212" class="reference internal">[settings] section</a>
    -   <a href="#filetype-extensions" id="toc-entry-213" class="reference internal">Filetype extensions</a>
    -   <a href="#preferences-file-format" id="toc-entry-214" class="reference internal">Preferences file format</a>
        -   <a href="#build-menu-section" id="toc-entry-215" class="reference internal">[build-menu] section</a>
            -   <a href="#menu-commands" id="toc-entry-216" class="reference internal">Menu commands</a>
            -   <a href="#error-regular-expression" id="toc-entry-217" class="reference internal">Error regular expression</a>
    -   <a href="#project-file-format" id="toc-entry-218" class="reference internal">Project file format</a>
        -   <a href="#build-menu-additions" id="toc-entry-219" class="reference internal">[build-menu] additions</a>
    -   <a href="#templates" id="toc-entry-220" class="reference internal">Templates</a>
        -   <a href="#template-meta-data" id="toc-entry-221" class="reference internal">Template meta data</a>
        -   <a href="#file-templates" id="toc-entry-222" class="reference internal">File templates</a>
            -   <a href="#adding-file-templates" id="toc-entry-223" class="reference internal">Adding file templates</a>
        -   <a href="#customizing-templates" id="toc-entry-224" class="reference internal">Customizing templates</a>
            -   <a href="#template-wildcards" id="toc-entry-225" class="reference internal">Template wildcards</a>
                -   <a href="#global-wildcards" id="toc-entry-226" class="reference internal">Global wildcards</a>
                -   <a href="#date-time-wildcards" id="toc-entry-227" class="reference internal">Date &amp; time wildcards</a>
                -   <a href="#dynamic-wildcards" id="toc-entry-228" class="reference internal">Dynamic wildcards</a>
                -   <a href="#template-insertion-wildcards" id="toc-entry-229" class="reference internal">Template insertion wildcards</a>
                -   <a href="#special-command-wildcard" id="toc-entry-230" class="reference internal">Special {command:} wildcard</a>
    -   <a href="#customizing-the-toolbar" id="toc-entry-231" class="reference internal">Customizing the toolbar</a>
        -   <a href="#manually-editing-the-toolbar-layout" id="toc-entry-232" class="reference internal">Manually editing the toolbar layout</a>
        -   <a href="#available-toolbar-elements" id="toc-entry-233" class="reference internal">Available toolbar elements</a>
-   <a href="#plugin-documentation" id="toc-entry-234" class="reference internal">Plugin documentation</a>
    -   <a href="#html-characters" id="toc-entry-235" class="reference internal">HTML Characters</a>
        -   <a href="#insert-entity-dialog" id="toc-entry-236" class="reference internal">Insert entity dialog</a>
        -   <a href="#replace-special-chars-by-its-entity" id="toc-entry-237" class="reference internal">Replace special chars by its entity</a>
            -   <a href="#at-typing-time" id="toc-entry-238" class="reference internal">At typing time</a>
            -   <a href="#bulk-replacement" id="toc-entry-239" class="reference internal">Bulk replacement</a>
    -   <a href="#save-actions" id="toc-entry-240" class="reference internal">Save Actions</a>
        -   <a href="#auto-save" id="toc-entry-241" class="reference internal">Auto Save</a>
            -   <a href="#save-on-focus-out" id="toc-entry-242" class="reference internal">Save on focus out</a>
        -   <a href="#backup-copy" id="toc-entry-243" class="reference internal">Backup Copy</a>
        -   <a href="#untitled-document-save" id="toc-entry-244" class="reference internal">Untitled Document Save</a>
            -   <a href="#instant-save" id="toc-entry-245" class="reference internal">Instant Save</a>
            -   <a href="#persistent-untitled-documents" id="toc-entry-246" class="reference internal">Persistent Untitled Documents</a>
-   <a href="#contributing-to-this-document" id="toc-entry-247" class="reference internal">Contributing to this document</a>
-   <a href="#scintilla-keyboard-commands" id="toc-entry-248" class="reference internal">Scintilla keyboard commands</a>
    -   <a href="#keyboard-commands" id="toc-entry-249" class="reference internal">Keyboard commands</a>
-   <a href="#tips-and-tricks" id="toc-entry-250" class="reference internal">Tips and tricks</a>
    -   <a href="#document-notebook" id="toc-entry-251" class="reference internal">Document notebook</a>
    -   <a href="#editor" id="toc-entry-252" class="reference internal">Editor</a>
    -   <a href="#sidebar-1" id="toc-entry-253" class="reference internal">Sidebar</a>
    -   <a href="#gtk-related" id="toc-entry-254" class="reference internal">GTK-related</a>
-   <a href="#compile-time-options" id="toc-entry-255" class="reference internal">Compile-time options</a>
    -   <a href="#src-geany-h" id="toc-entry-256" class="reference internal">src/geany.h</a>
    -   <a href="#project-h" id="toc-entry-257" class="reference internal">project.h</a>
    -   <a href="#filetypes-c" id="toc-entry-258" class="reference internal">filetypes.c</a>
    -   <a href="#editor-h" id="toc-entry-259" class="reference internal">editor.h</a>
    -   <a href="#keyfile-c" id="toc-entry-260" class="reference internal">keyfile.c</a>
    -   <a href="#build-c" id="toc-entry-261" class="reference internal">build.c</a>
-   <a href="#gnu-general-public-license" id="toc-entry-262" class="reference internal">GNU General Public License</a>
-   <a href="#license-for-scintilla-and-scite" id="toc-entry-263" class="reference internal">License for Scintilla and SciTE</a>

</div>

<div id="introduction" class="section">

# <a href="#toc-entry-1" class="toc-backref">Introduction</a>

<div id="about-geany" class="section">

## <a href="#toc-entry-2" class="toc-backref">About Geany</a>

Geany is a small and lightweight Integrated Development Environment. It was developed to provide a small and fast IDE, which has only a few dependencies on other packages. Another goal was to be as independent as possible from a particular Desktop Environment like KDE or GNOME - Geany only requires the GTK+ runtime libraries.

Some basic features of Geany:

-   Syntax highlighting
-   Code folding
-   Autocompletion of symbols/words
-   Construct completion/snippets
-   Auto-closing of XML and HTML tags
-   Calltips
-   Many supported filetypes including C, Java, PHP, HTML, Python, Perl, Pascal, and others
-   Symbol lists
-   Code navigation
-   Build system to compile and execute your code
-   Simple project management
-   Plugin interface

</div>

<div id="where-to-get-it" class="section">

## <a href="#toc-entry-3" class="toc-backref">Where to get it</a>

You can obtain Geany from <a href="https://www.geany.org/" class="reference external">https://www.geany.org/</a> or perhaps also from your distribution. For a list of available packages, please see <a href="https://www.geany.org/Download/ThirdPartyPackages" class="reference external">https://www.geany.org/Download/ThirdPartyPackages</a>.

</div>

<div id="license" class="section">

## <a href="#toc-entry-4" class="toc-backref">License</a>

Geany is distributed under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. A copy of this license can be found in the file COPYING included with the source code of this program and in the chapter, <a href="#gnu-general-public-license" class="reference internal">GNU General Public License</a>.

The included Scintilla library (found in the subdirectory scintilla/) has its own license, which can be found in the chapter, <a href="#license-for-scintilla-and-scite" class="reference internal">License for Scintilla and SciTE</a>.

</div>

<div id="about-this-document" class="section">

## <a href="#toc-entry-5" class="toc-backref">About this document</a>

This documentation is available in HTML and text formats. The latest version can always be found at <a href="https://www.geany.org/" class="reference external">https://www.geany.org/</a>.

If you want to contribute to it, see <a href="#contributing-to-this-document" class="reference internal">Contributing to this document</a>.

</div>

</div>

<div id="installation" class="section">

# <a href="#toc-entry-6" class="toc-backref">Installation</a>

<div id="requirements" class="section">

## <a href="#toc-entry-7" class="toc-backref">Requirements</a>

You will need the GTK (\>= 3.24) libraries and their dependencies (Pango, GLib and ATK). Your distro should provide packages for these, usually installed by default. For Windows, you can download an installer from the website which bundles these libraries.

</div>

<div id="binary-packages" class="section">

## <a href="#toc-entry-8" class="toc-backref">Binary packages</a>

There are many binary packages available. For an up-to-date but maybe incomplete list see <a href="https://www.geany.org/Download/ThirdPartyPackages" class="reference external">https://www.geany.org/Download/ThirdPartyPackages</a>.

</div>

<div id="source-compilation" class="section">

## <a href="#toc-entry-9" class="toc-backref">Source compilation</a>

Compiling Geany is quite easy. To do so, you need the GTK (\>= 3.24) libraries and header files. You also need the Pango, GLib and ATK libraries and header files. All these files are available at <a href="https://www.gtk.org" class="reference external">https://www.gtk.org</a>, but very often your distro will provide development packages to save the trouble of building these yourself.

Furthermore you need, of course, a C and C++ compiler. The GNU versions of these tools are recommended.

<div id="autotools-based-build-system" class="section">

### <a href="#toc-entry-10" class="toc-backref">Autotools based build system</a>

To compile Geany yourself, you just need the Make tool, preferably GNU Make.

Then run the following commands:

``` literal-block
$ ./configure
$ make
```

Then as root:

``` literal-block
% make install
```

Or via sudo:

``` literal-block
% sudo make install
```

</div>

<div id="custom-installation" class="section">

### <a href="#toc-entry-11" class="toc-backref">Custom installation</a>

The configure script supports several common options, for a detailed list, type:

``` literal-block
$ ./configure --help
```

You may also want to read the INSTALL file for advanced installation options.

-   See also <a href="#compile-time-options" class="reference internal">Compile-time options</a>.

</div>

<div id="dynamic-linking-loader-support-and-vte" class="section">

### <a href="#toc-entry-12" class="toc-backref">Dynamic linking loader support and VTE</a>

In the case that your system lacks dynamic linking loader support, you probably want to pass the option <span class="pre">--disable-vte</span> to the configure script. This prevents compiling Geany with dynamic linking loader support for automatically loading libvte.so.4 if available.

</div>

<div id="build-problems" class="section">

### <a href="#toc-entry-13" class="toc-backref">Build problems</a>

If there are any errors during compilation, check your build environment and try to find the error, otherwise contact the mailing list or one the authors. Sometimes you might need to ask for specific help from your distribution.

</div>

</div>

<div id="installation-prefix" class="section">

## <a href="#toc-entry-14" class="toc-backref">Installation prefix</a>

If you want to find Geany's system files after installation you may want to know the installation prefix.

Pass the <span class="pre">--print-prefix</span> option to Geany to check this - see <a href="#command-line-options" class="reference internal">Command line options</a>. The first path is the prefix.

On Unix-like systems this is commonly /usr if you installed from a binary package, or /usr/local if you build from source.

<div class="admonition note">

Note

Editing system files is not necessary as you should use the per-user configuration files instead, which don't need root permissions. See <a href="#configuration-files" class="reference internal">Configuration files</a>.

</div>

</div>

</div>

<div id="usage" class="section">

# <a href="#toc-entry-15" class="toc-backref">Usage</a>

<div id="getting-started" class="section">

## <a href="#toc-entry-16" class="toc-backref">Getting started</a>

You can start Geany in the following ways:

-   From the Desktop Environment menu:

    Choose in your application menu of your used Desktop Environment: Development --\> Geany.

    At Windows-systems you will find Geany after installation inside the application menu within its special folder.

-   From the command line:

    To start Geany from a command line, type the following and press Return:

    ``` literal-block
    % geany
    ```

</div>

<div id="the-geany-workspace" class="section">

## <a href="#toc-entry-17" class="toc-backref">The Geany workspace</a>

The Geany window is shown in the following figure:

![](./images/main_window.png)

<div class="admonition note">

Note

Screenshots in this document are taken with the default GTK Adwaita theme, but Geany will adapt to the desktop GTK theme that is set.

</div>

The workspace has the following parts:

-   The menu.
-   An optional toolbar.
-   An optional sidebar that can show the following tabs:
    -   Documents - A <a href="#document-list-views" class="reference external">document list</a>.
    -   Symbols - A list of symbols in your code.
-   The main editor window.
-   An optional message window which can show the following tabs:
    -   Status - A list of status messages.
    -   Compiler - The output of compiling or building programs.
    -   Messages - Results of <a href="#find-usage" class="reference internal">Find Usage</a>, <a href="#find-in-files" class="reference internal">Find in Files</a> and other actions
    -   Scribble - A text scratchpad for any use.
    -   Terminal - An optional <a href="#virtual-terminal-emulator-widget-vte" class="reference external">terminal window</a>.
-   A status bar

Most of these can be configured in the <a href="#interface-preferences" class="reference internal">Interface preferences</a>, the <a href="#view-menu" class="reference internal">View menu</a>, or the popup menu for the relevant area.

Additional tabs may be added to the sidebar and message window by plugins.

The position of the tabs can be selected in the interface preferences.

The sizes of the sidebar and message window can be adjusted by dragging the dividers.

<div id="sidebar-usage" class="section">

### <a href="#toc-entry-18" class="toc-backref">Sidebar Usage</a>

The sidebar has a right click menu that can control what is visible and has actions specific to the tab (other tabs added by plugins are described by that plugin documentation):

-   Symbols

    -   expand/collapse the tree
    -   control sorting order
    -   control whether to group symbols by their type
    -   locate the symbol in documents

    The symbols tab can also be filtered by typing a string into the entry at the top of the tab. All symbols that contain the entered string as a substring will be shown in the tree. Multiple filters can be separated by a space.

-   Documents

    -   expand/collapse the tree
    -   save to or reload from files
    -   search tree based at selected file
    -   show or hide the document paths
    -   filter documents based on their name similarly to the Symbols tab

</div>

</div>

<div id="command-line-options" class="section">

## <a href="#toc-entry-19" class="toc-backref">Command line options</a>

<table class="docutils" style="width:99%;" data-border="1">
<colgroup>
<col style="width: 9%" />
<col style="width: 18%" />
<col style="width: 72%" />
</colgroup>
<thead data-valign="bottom">
<tr class="header">
<th class="head">Short option</th>
<th class="head">Long option</th>
<th class="head">Function</th>
</tr>
</thead>
<tbody data-valign="top">
<tr class="odd">
<td><em>none</em></td>
<td>+number</td>
<td>Set initial line number for the first opened file (same as --line, do not put a space between the + sign and the number). E.g. "geany +7 foo.bar" will open the file foo.bar and place the cursor in line 7.</td>
</tr>
<tr class="even">
<td><em>none</em></td>
<td>--column</td>
<td>Set initial column number for the first opened file.</td>
</tr>
<tr class="odd">
<td>-c dir_name</td>
<td>--config=directory_name</td>
<td>Use an alternate configuration directory. The default configuration directory is <span class="pre">~/.config/geany/</span> and that is where geany.conf and other configuration files reside.</td>
</tr>
<tr class="even">
<td><em>none</em></td>
<td>--ft-names</td>
<td>Print a list of Geany's internal filetype names (useful for snippets configuration).</td>
</tr>
<tr class="odd">
<td>-g</td>
<td>--generate-tags</td>
<td>Generate a global tags file (see <a href="#generating-a-global-tags-file" class="reference internal">Generating a global tags file</a>).</td>
</tr>
<tr class="even">
<td>-P</td>
<td>--no-preprocessing</td>
<td>Don't preprocess C/C++ files when generating tags file.</td>
</tr>
<tr class="odd">
<td>-i</td>
<td>--new-instance</td>
<td>Do not open files in a running instance, force opening a new instance. Only available if Geany was compiled with support for Sockets.</td>
</tr>
<tr class="even">
<td>-l</td>
<td>--line</td>
<td>Set initial line number for the first opened file.</td>
</tr>
<tr class="odd">
<td><em>none</em></td>
<td>--list-documents</td>
<td>Return a list of open documents in a running Geany instance. This can be used to read the currently opened documents in Geany from an external script or tool. The returned list is separated by newlines (LF) and consists of the full, UTF-8 encoded filenames of the documents. Only available if Geany was compiled with support for Sockets.</td>
</tr>
<tr class="even">
<td>-m</td>
<td>--no-msgwin</td>
<td>Do not show the message window. Use this option if you do not need compiler messages or VTE support.</td>
</tr>
<tr class="odd">
<td>-n</td>
<td>--no-ctags</td>
<td>Do not load symbol completion and call tip data. Use this option if you do not want to use them.</td>
</tr>
<tr class="even">
<td>-p</td>
<td>--no-plugins</td>
<td>Do not load plugins or plugin support.</td>
</tr>
<tr class="odd">
<td><em>none</em></td>
<td>--print-prefix</td>
<td>Print installation prefix, the data directory, the lib directory and the locale directory (in that order) to stdout, one line each. This is mainly intended for plugin authors to detect installation paths.</td>
</tr>
<tr class="even">
<td>-r</td>
<td>--read-only</td>
<td>Open all files given on the command line in read-only mode. This only applies to files opened explicitly from the command line, so files from previous sessions or project files are unaffected.</td>
</tr>
<tr class="odd">
<td>-s</td>
<td>--no-session</td>
<td>Do not load the previous session's files.</td>
</tr>
<tr class="even">
<td>-t</td>
<td>--no-terminal</td>
<td>Do not load terminal support. Use this option if you do not want to load the virtual terminal emulator widget at startup. If you do not have libvte.so.4 installed, then terminal-support is automatically disabled. Only available if Geany was compiled with support for VTE.</td>
</tr>
<tr class="odd">
<td><em>none</em></td>
<td>--socket-file</td>
<td><p>Use this socket filename for communication with a running Geany instance. This can be used with the following command to execute Geany on the current workspace:</p>
<pre class="last literal-block"><code>geany --socket-file=/tmp/geany-sock-$(xprop -root _NET_CURRENT_DESKTOP | awk &#39;{print $3}&#39;)</code></pre></td>
</tr>
<tr class="even">
<td><em>none</em></td>
<td>--vte-lib</td>
<td>Specify explicitly the path including filename or only the filename to the VTE library, e.g. /usr/lib/libvte.so or libvte.so. This option is only needed when the auto-detection does not work. Only available if Geany was compiled with support for VTE.</td>
</tr>
<tr class="odd">
<td>-v</td>
<td>--verbose</td>
<td>Be verbose (print useful status messages).</td>
</tr>
<tr class="even">
<td>-V</td>
<td>--version</td>
<td>Show version information and exit.</td>
</tr>
<tr class="odd">
<td>-?</td>
<td>--help</td>
<td>Show help information and exit.</td>
</tr>
<tr class="even">
<td><em>none</em></td>
<td><p><em>files ...</em></p>
<p><em>file:line ...</em></p>
<p><em>file:line:col ...</em></p></td>
<td><p>Open all given filenames at startup. If a running instance is detected, pass filenames to it instead.</p>
<p>Geany also recognizes line and column information when appended to the filename with colons, e.g. geany foo.bar:10:5 will open the file foo.bar and place the cursor in line 10 at column 5.</p>
<p>If a filename does not exist, create a new document with the desired filename if the <em>Open new files from the command-line</em> <a href="#files-preferences" class="reference external">file pref</a> is set.</p>
<p>A project can also be opened, but the project filename (*.geany) must be the first non-option argument. Any other project filenames will be opened as text files.</p></td>
</tr>
</tbody>
</table>

Geany also supports all generic GTK options, a list is available on the help screen.

</div>

<div id="general" class="section">

## <a href="#toc-entry-20" class="toc-backref">General</a>

<div id="startup" class="section">

### <a href="#toc-entry-21" class="toc-backref">Startup</a>

At startup, Geany loads all files from the last time Geany was launched. You can disable this feature in the preferences dialog (see <a href="#general-startup-preferences" class="reference internal">General Startup preferences</a>).

You can start several instances of Geany, but only the first will load files from the last session. In the subsequent instances, you can find these files in the file menu under the *Recent files* item. By default this contains the last 10 recently opened files. You can change the number of recently opened files in the <a href="#files-preferences" class="reference external">Files tab</a> of the preferences dialog.

To run a second instance of Geany, do not specify any filenames on the command-line, or disable opening files in a running instance using the <span class="pre">-i</span> <a href="#command-line-options" class="reference external">command line option</a>.

</div>

<div id="opening-files" class="section">

### <a href="#toc-entry-22" class="toc-backref">Opening files</a>

<div id="open-dialog" class="section">

#### <a href="#toc-entry-23" class="toc-backref">Open dialog</a>

The *File-\>Open* command will show a dialog to choose one or more text files to open. There is a list of file filters on the right with the following items:

-   All files (default)
-   All source - a combination of all the patterns for each filetype (see <a href="#filetype-extensions" class="reference internal">Filetype extensions</a>)
-   Individual filetypes

Clicking *More options* will reveal controls to open files with a specific filetype and/or encoding (see <a href="#character-sets-and-unicode-byte-order-mark-bom" class="reference internal">Character sets and Unicode Byte-Order-Mark (BOM)</a>).

</div>

<div id="opening-files-from-the-command-line-in-a-running-instance" class="section">

#### <a href="#toc-entry-24" class="toc-backref">Opening files from the command-line in a running instance</a>

Geany detects if there is an instance of itself already running and opens files from the command-line in that instance. So, Geany can be used to view and edit files by opening them from other programs such as a file manager.

You can also pass line number and column number information, e.g.:

``` literal-block
geany some_file.foo:55:4
```

This would open the file some_file.foo with the cursor on line 55, column 4.

If you do not like this for some reason, you can disable using the first instance by using the appropriate command line option -- see the section called <a href="#command-line-options" class="reference internal">Command line options</a>.

</div>

</div>

<div id="virtual-terminal-emulator-widget-vte" class="section">

### <a href="#toc-entry-25" class="toc-backref">Virtual terminal emulator widget (VTE)</a>

If you have installed libvte.so on your system, it is loaded automatically by Geany, and you will have a terminal widget in the notebook at the bottom.

If Geany cannot find any libvte.so at startup, the terminal widget will not be loaded. So there is no need to install the package containing this file in order to run Geany. Additionally, you can disable the use of the terminal widget by command line option, for more information see the section called <a href="#command-line-options" class="reference internal">Command line options</a>.

You can use this terminal (from now on called VTE) much as you would a terminal program like xterm. There is basic clipboard support. You can paste the contents of the clipboard by pressing the right mouse button to open the popup menu, and choosing Paste. To copy text from the VTE, just select the desired text and then press the right mouse button and choose Copy from the popup menu. On systems running the X Window System you can paste the last selected text by pressing the middle mouse button in the VTE (on 2-button mice, the middle button can often be simulated by pressing both mouse buttons together).

In the preferences dialog you can specify a shell which should be started in the VTE. To make the specified shell a login shell just use the appropriate command line options for the shell. These options should be found in the manual page of the shell. For zsh and bash you can use the argument <span class="pre">--login</span>.

<div class="admonition note">

Note

Geany tries to load libvte.so. If this fails, it tries to load some other filenames. If this fails too, you should check whether you installed libvte correctly. Again note, Geany will run without this library.

</div>

It could be, that the library is called something else than libvte.so (e.g. on FreeBSD 6.0 it is called libvte.so.8). If so please set a link to the correct file (as root):

``` literal-block
# ln -s /usr/lib/libvte.so.X /usr/lib/libvte.so
```

Obviously, you have to adjust the paths and set X to the number of your libvte.so.

You can also specify the filename of the VTE library to use on the command line (see the section called <a href="#command-line-options" class="reference internal">Command line options</a>) or at compile time by specifying the command line option <span class="pre">--with-vte-module-path</span> to ./configure.

</div>

</div>

<div id="documents" class="section">

## <a href="#toc-entry-26" class="toc-backref">Documents</a>

<div id="switching-between-documents" class="section">

### <a href="#toc-entry-27" class="toc-backref">Switching between documents</a>

The documents list and the editor tabs are two different ways to switch between documents using the mouse. When you hit the key combination to move between tabs, the order is determined by the tab order. It is not alphabetical as shown in the documents list (regardless of whether or not editor tabs are visible).

See the <a href="#notebook-tab-keybindings" class="reference internal">Notebook tab keybindings</a> section for useful shortcuts including for Most-Recently-Used document switching.

</div>

<div id="document-list-views" class="section">

### <a href="#toc-entry-28" class="toc-backref">Document list views</a>

There are three different ways to display documents on the sidebar if *Show documents list* is active. To switch between views press the right mouse button on the documents list and select one of these items:

Documents Only  
Show only file names of open documents in sorted order.

<img src="./images/sidebar_documents_only.png" class="last" alt="./images/sidebar_documents_only.png" />

Show Paths  
Show open documents as a two-level tree in which first level is the paths of directories containing open files and the second level is the file names of the documents open in that path. All documents with the same path are grouped together under the same first level item. Paths are in sorted order and documents are sorted within each group.

<img src="./images/sidebar_show_paths.png" class="last" alt="./images/sidebar_show_paths.png" />

Show Tree  
Show paths as above, but as a multiple level partial tree. The tree is only expanded at positions where two or more directory paths to open documents share the same prefix. The common prefix is shown as a parent level, and the remainder of those paths are shown as child levels. This applies recursively down the paths making a tree to the file names of open documents, which are grouped in sorted order as an additional level below the last path segment.

For convenience two common file locations are handled specially, open files below the users home directory and open files below an open project base path. Each of these is moved to its own top level tree instead of being in place in the normal tree. The top level of these trees are each labelled differently. For the home directory tree the path of the home directory is shown as \~, and for the project tree the path to the project base path is shown simply as the project name.

<img src="./images/sidebar_show_tree.png" class="last" alt="./images/sidebar_show_tree.png" />

In all cases paths and file names that do not fit in the width available are ellipsised.

</div>

<div id="cloning-documents" class="section">

### <a href="#toc-entry-29" class="toc-backref">Cloning documents</a>

The Document-\>Clone menu item copies the current document's text, cursor position and properties into a new untitled document. If there is a selection, only the selected text is copied. This can be useful when making temporary copies of text or for creating documents with similar or identical contents.

</div>

<div id="automatic-filename-insertion-on-save-as" class="section">

### <a href="#toc-entry-30" class="toc-backref">Automatic filename insertion on Save As...</a>

If a document is saved via Document-\>Save As... then the filename is automatically inserted into the comment header replacing text like untitled.ext in the first 3 lines of the file. E.g. if a new .c file is created using File-\>New (with Template) then the text untitled.c in line 2 would be replaced with the chosen file name on Save As... (this example assumes the default file templates being used).

</div>

</div>

<div id="character-sets-and-unicode-byte-order-mark-bom" class="section">

## <a href="#toc-entry-31" class="toc-backref">Character sets and Unicode Byte-Order-Mark (BOM)</a>

<div id="using-character-sets" class="section">

### <a href="#toc-entry-32" class="toc-backref">Using character sets</a>

Geany provides support for detecting and converting character sets. So you can open and save files in different character sets, and even convert a file from one character set to another. To do this, Geany uses the character conversion capabilities of the GLib library.

Only text files are supported, i.e. opening files which contain NULL-bytes may fail. Geany will try to open the file anyway but it is likely that the file will be truncated because it can only be read up to the first occurrence of a NULL-byte. All characters after this position are lost and are not written when you save the file.

Geany tries to detect the encoding of a file while opening it, but auto-detecting the encoding of a file is not easy and sometimes an encoding might not be detected correctly. In this case you have to set the encoding of the file manually in order to display it correctly. You can this in the file open dialog by selecting an encoding in the drop down box or by reloading the file with the file menu item "Reload as". The auto-detection works well for most encodings but there are also some encodings where it is known that auto-detection has problems.

There are different ways to set different encodings in Geany:

-   Using the file open dialog

    This opens the file with the encoding specified in the encoding drop down box. If the encoding is set to "Detect from file" auto-detection will be used. If the encoding is set to "Without encoding (None)" the file will be opened without any character conversion and Geany will not try to auto-detect the encoding (see below for more information).

-   Using the "Reload as" menu item

    This item reloads the current file with the specified encoding. It can help if you opened a file and found out that the wrong encoding was used.

-   Using the "Set encoding" menu item

    Contrary to the above two options, this will not change or reload the current file unless you save it. It is useful when you want to change the encoding of the file.

-   Specifying the encoding in the file itself

    As mentioned above, auto-detecting the encoding of a file may fail on some encodings. If you know that Geany doesn't open a certain file, you can add the specification line, described in the next section, to the beginning of the file to force Geany to use a specific encoding when opening the file.

</div>

<div id="in-file-encoding-specification" class="section">

### <a href="#toc-entry-33" class="toc-backref">In-file encoding specification</a>

Geany detects meta tags of HTML files which contain charset information like:

``` literal-block
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-15" />
```

and the specified charset is used when opening the file. This is useful if the encoding of the file cannot be detected properly. For non-HTML files you can also define a line like:

``` literal-block
/* geany_encoding=ISO-8859-15 */
```

or:

``` literal-block
# geany_encoding=ISO-8859-15 #
```

to force an encoding to be used. The \#, /\* and \*/ are examples of filetype-specific comment characters. It doesn't matter which characters are around the string " geany_encoding=ISO-8859-15 " as long as there is at least one whitespace character before and after this string. Whitespace characters are in this case a space or tab character. An example to use this could be you have a file with ISO-8859-15 encoding but Geany constantly detects the file encoding as ISO-8859-1. Then you simply add such a line to the file and Geany will open it correctly the next time.

Since Geany 0.15 you can also use lines which match the regular expression used to find the encoding string: <span class="pre">coding\[\\t</span> <span class="pre">\]\*\[:=\]\[\\t</span> <span class="pre">\]\*(\[a-z0-9-\]+)\[\\t</span> \]\*

<div class="admonition note">

Note

These specifications must be in the first 512 bytes of the file. Anything after the first 512 bytes will not be recognized.

</div>

Some examples are:

``` literal-block
# encoding = ISO-8859-15
```

or:

``` literal-block
# coding: ISO-8859-15
```

</div>

<div id="special-encoding-none" class="section">

### <a href="#toc-entry-34" class="toc-backref">Special encoding "None"</a>

There is a special encoding "None" which uses no encoding. It is useful when you know that Geany cannot auto-detect the encoding of a file and it is not displayed correctly. Especially when the file contains NULL-bytes this can be useful to skip auto detection and open the file properly at least until the occurrence of the first NULL-byte. Using this encoding opens the file as it is without any character conversion.

</div>

<div id="unicode-byte-order-mark-bom" class="section">

### <a href="#toc-entry-35" class="toc-backref">Unicode Byte-Order-Mark (BOM)</a>

Furthermore, Geany detects a Unicode Byte Order Mark (see <a href="https://en.wikipedia.org/wiki/Byte_Order_Mark" class="reference external">https://en.wikipedia.org/wiki/Byte_Order_Mark</a> for details). Of course, this feature is only available if the opened file is in a Unicode encoding. The Byte Order Mark helps to detect the encoding of a file, e.g. whether it is UTF-16LE or UTF-16BE and so on. On Unix-like systems using a Byte Order Mark could cause some problems for programs not expecting it, e.g. the compiler gcc stops with stray errors, PHP does not parse a script containing a BOM and script files starting with a she-bang maybe cannot be started. In the status bar you can easily see whether the file starts with a BOM or not.

If you want to set a BOM for a file or if you want to remove it from a file, just use the document menu and toggle the checkbox.

<div class="admonition note">

Note

If you are unsure what a BOM is or if you do not understand where to use it, then it is probably not important for you and you can safely ignore it.

</div>

</div>

</div>

<div id="editing" class="section">

## <a href="#toc-entry-36" class="toc-backref">Editing</a>

<div id="folding" class="section">

### <a href="#toc-entry-37" class="toc-backref">Folding</a>

Geany provides basic code folding support. Folding means the ability to show and hide parts of the text in the current file. You can hide unimportant code sections and concentrate on the parts you are working on and later you can show hidden sections again. In the editor window there is a small grey margin on the left side with \[+\] and \[-\] symbols which show hidden parts and hide parts of the file respectively. By clicking on these icons you can simply show and hide sections which are marked by vertical lines within this margin. For many filetypes nested folding is supported, so there may be several fold points within other fold points.

<div class="admonition note">

Note

You can customize the folding icon and line styles - see the filetypes.common <a href="#folding-settings" class="reference internal">Folding Settings</a>.

</div>

If you don't like it or don't need it at all, you can simply disable folding support completely in the preferences dialog.

The folding behaviour can be changed with the "Fold/Unfold all children of a fold point" option in the preference dialog. If activated, Geany will unfold all nested fold points below the current one if they are already folded (when clicking on a \[+\] symbol). When clicking on a \[-\] symbol, Geany will fold all nested fold points below the current one if they are unfolded.

This option can be inverted by pressing the Shift key while clicking on a fold symbol. That means, if the "Fold/Unfold all children of a fold point" option is enabled, pressing Shift will disable it for this click and vice versa.

</div>

<div id="column-mode-editing-rectangular-selections" class="section">

### <a href="#toc-entry-38" class="toc-backref">Column mode editing (rectangular selections)</a>

There is basic support for column mode editing. To use it, create a rectangular selection by holding down the Control and Shift keys (or Alt and Shift on Windows) while selecting some text using the mouse. To create a rectangular selection using the keyboard only, hold down the Alt and Shift keys while using the cursor keys to select some text. Once a rectangular selection exists you can start editing the text within this selection and the modifications will be done for every line in the selection.

It is also possible to create a zero-column selection - this is useful to insert text on multiple lines.

</div>

<div id="drag-and-drop-of-text" class="section">

### <a href="#toc-entry-39" class="toc-backref">Drag and drop of text</a>

If you drag selected text in the editor widget of Geany the text is moved to the position where the mouse pointer is when releasing the mouse button. Holding Control when releasing the mouse button will copy the text instead. This behaviour was changed in Geany 0.11 - before the selected text was copied to the new position.

</div>

<div id="indentation" class="section">

### <a href="#toc-entry-40" class="toc-backref">Indentation</a>

Geany allows each document to indent either with a tab character, multiple spaces or a combination of both.

The *Tabs* setting indents with one tab character per indent level, and displays tabs as the indent width.

The *Spaces* setting indents with the number of spaces set in the indent width for each level.

The *Tabs and Spaces* setting indents with spaces as above, then converts as many spaces as it can to tab characters at the rate of one tab for each multiple of the Various preference setting *indent_hard_tab_width* (default 8) and displays tabs as the *indent_hard_tab_width* value.

The default indent settings are set in <a href="#editor-indentation-preferences" class="reference internal">Editor Indentation preferences</a> (see the link for more information).

The default settings can be overridden per-document using the Document menu. They can also be overridden by projects - see <a href="#project-management" class="reference internal">Project management</a>.

The indent mode for the current document is shown on the status bar as follows:

TAB  
Indent with Tab characters.

SP  
Indent with spaces.

T/S  
Indent with tabs and spaces, depending on how much indentation is on a line.

<div id="applying-new-indentation-settings" class="section">

#### <a href="#toc-entry-41" class="toc-backref">Applying new indentation settings</a>

After changing the default settings you may wish to apply the new settings to every document in the current session. To do this use the *Project-\>Apply Default Indentation* menu item.

</div>

<div id="detecting-indent-type" class="section">

#### <a href="#toc-entry-42" class="toc-backref">Detecting indent type</a>

The *Detect from file* indentation preference can be used to scan each file as it's opened and set the indent type based on how many lines start with a tab vs. 2 or more spaces.

</div>

</div>

<div id="auto-indentation" class="section">

### <a href="#toc-entry-43" class="toc-backref">Auto-indentation</a>

When enabled, auto-indentation happens when pressing *Enter* in the Editor. It adds a certain amount of indentation to the new line so the user doesn't always have to indent each line manually.

Geany has four types of auto-indentation:

None  
Disables auto-indentation completely.

Basic  
Adds the same amount of whitespace on a new line as on the previous line. For the *Tabs* and the *Spaces* indent types the indentation will use the same combination of characters as the previous line. The *Tabs and Spaces* indentation type converts as explained above.

Current chars  
Does the same as *Basic* but also indents a new line after an opening brace '{', and de-indents when typing a closing brace '}'. For Python, a new line will be indented after typing ':' at the end of the previous line.

Match braces  
Similar to *Current chars* but the closing brace will be aligned to match the indentation of the line with the opening brace. This requires the filetype to be one where Geany knows that the Scintilla lexer understands matching braces (C, C++, D, HTML, Pascal, Bash, Perl, TCL).

There is also XML-tag auto-indentation. This is enabled when the mode is more than just Basic, and is also controlled by a filetype setting - see <a href="#xml-indent-tags" class="reference internal">xml_indent_tags</a>.

</div>

<div id="bookmarks" class="section">

### <a href="#toc-entry-44" class="toc-backref">Bookmarks</a>

Geany provides a handy bookmarking feature that lets you mark one or more lines in a document, and return the cursor to them using a key combination.

To place a mark on a line, either left-mouse-click in the left margin of the editor window, or else use Ctrl-m. This will produce a small green plus symbol in the margin. You can have as many marks in a document as you like. Click again (or use Ctrl-m again) to remove the bookmark. To remove all the marks in a given document, use "Remove Markers" in the Document menu.

To navigate down your document, jumping from one mark to the next, use Ctrl-. (control period). To go in the opposite direction on the page, use Ctrl-, (control comma). Using the bookmarking feature together with the commands to switch from one editor tab to another (Ctrl-PgUp/PgDn and Ctrl-Tab) provides a particularly fast way to navigate around multiple files.

</div>

<div id="code-navigation-history" class="section">

### <a href="#toc-entry-45" class="toc-backref">Code navigation history</a>

To ease navigation in source files and especially between different files, Geany lets you jump between different navigation points. Currently, this works for the following:

-   <a href="#go-to-symbol-declaration" class="reference internal">Go to symbol declaration</a>
-   <a href="#go-to-symbol-definition" class="reference internal">Go to symbol definition</a>
-   Symbol list items
-   Build errors
-   Message items

When using one of these actions, Geany remembers your current position and jumps to the new one. If you decide to go back to your previous position in the file, just use "Navigate back a location". To get back to the new position again, just use "Navigate forward a location". This makes it easier to navigate in e.g. foreign code and between different files.

</div>

<div id="sending-text-through-custom-commands" class="section">

### <a href="#toc-entry-46" class="toc-backref">Sending text through custom commands</a>

You can define several custom commands in Geany and send the current selection to one of these commands using the *Edit-\>Format-\>Send Selection to* menu or keybindings. The output of the command will be used to replace the current selection. This makes it possible to use text formatting tools with Geany in a general way.

The selected text will be sent to the standard input of the executed command, so the command should be able to read from it and it should print all results to its standard output which will be read by Geany. To help finding errors in executing the command, the output of the program's standard error will be printed on Geany's standard output.

If there is no selection, the whole current line is used instead.

To add a custom command, use the *Send Selection to-\>Set Custom Commands* menu item. Click on *Add* to get a new item and type the command. You can also specify some command line options. Empty commands are not saved.

Normal shell quoting is supported, so you can do things like:

-   sed <span class="pre">'s/\\./(dot)/g'</span>

The above example would normally be done with the <a href="#replace-all" class="reference internal">Replace all</a> function, but it can be handy to have common commands already set up.

Note that the command is not run in a shell, so if you want to use shell features like pipes and command chains, you need to explicitly launch the shell and pass it your command:

-   sh <span class="pre">-c</span> 'sort \| uniq'

</div>

<div id="context-actions" class="section">

### <a href="#toc-entry-47" class="toc-backref">Context actions</a>

You can execute the context action command on the current word at the cursor position or the available selection. This word or selection can be used as an argument to the command. The context action is invoked by a menu entry in the popup menu of the editor and also a keyboard shortcut (see the section called <a href="#keybindings" class="reference internal">Keybindings</a>).

The command can be specified in the preferences dialog and also for each filetype (see "context_action_cmd" in the section called <a href="#filetype-configuration" class="reference internal">Filetype configuration</a>). When the context action is invoked, the filetype specific command is used if available, otherwise the command specified in the preferences dialog is executed.

The current word or selection can be referred with the wildcard "%s" in the command, it will be replaced by the current word or selection before the command is executed.

For example a context action can be used to open API documentation in a browser window, the command to open the PHP API documentation would be:

``` literal-block
firefox "https://www.php.net/%s"
```

when executing the command, the %s is substituted by the word near the cursor position or by the current selection. If the cursor is at the word "echo", a browser window will open(assumed your browser is called firefox) and it will open the address: <a href="https://www.php.net/echo" class="reference external">https://www.php.net/echo</a>.

</div>

<div id="autocompletion" class="section">

### <a href="#toc-entry-48" class="toc-backref">Autocompletion</a>

Geany can offer a list of possible completions for symbols defined in the tags files and for all words in open documents.

The autocompletion list for symbols is presented when the first few characters of the symbol are typed (configurable, see <a href="#editor-completions-preferences" class="reference internal">Editor Completions preferences</a>, default 4) or when the *Complete word* keybinding is pressed (configurable, see <a href="#editor-keybindings" class="reference internal">Editor keybindings</a>, default Ctrl-Space).

For some languages the autocompletion list is ordered by heuristics to attempt to show names that are more likely to be what the user wants close to the top of the list.

When the defined keybinding is typed and the *Autocomplete all words in document* preference (in <a href="#editor-completions-preferences" class="reference internal">Editor Completions preferences</a>) is selected then the autocompletion list will show all matching words in the document, if there are no matching symbols.

If you don't want to use autocompletion it can be dismissed until the next symbol by pressing Escape. The autocompletion list is updated as more characters are typed so that it only shows completions that start with the characters typed so far. If no symbols begin with the sequence, the autocompletion window is closed.

The up and down arrows will move the selected item. The highlighted item on the autocompletion list can be chosen from the list by pressing Enter/Return. You can also double-click to select an item. The sequence will be completed to match the chosen item, and if the *Drop rest of word on completion* preference is set (in <a href="#editor-completions-preferences" class="reference internal">Editor Completions preferences</a>) then any characters after the cursor that match a symbol or word are deleted.

<div id="word-part-completion" class="section">

#### <a href="#toc-entry-49" class="toc-backref">Word part completion</a>

By default, pressing Tab will complete the selected item by word part; useful e.g. for adding the prefix gtk_combo_box_entry\_ without typing it manually:

-   gtk_com\<TAB\>
-   gtk_combo\_\<TAB\>
-   gtk_combo_box\_\<e\>\<TAB\>
-   gtk_combo_box_entry\_\<s\>\<ENTER\>
-   gtk_combo_box_entry_set_text_column

The key combination can be changed from Tab - See <a href="#editor-keybindings" class="reference internal">Editor keybindings</a>. If you clear/change the key combination for word part completion, Tab will complete the whole word instead, like Enter.

</div>

<div id="scope-autocompletion" class="section">

#### <a href="#toc-entry-50" class="toc-backref">Scope autocompletion</a>

E.g.:

``` literal-block
struct
{
    int i;
    char c;
} foo;
```

When you type foo. it will show an autocompletion list with 'i' and 'c' symbols.

It only works for languages that set parent scope names for e.g. struct members. Most languages only parse global definitions and so scope autocompletion will not work for names declared in local scope (e.g. inside functions). A few languages parse both local and global symbols (e.g. C/C++ parsers) and for these parsers scope autocompletion works also for local variables.

</div>

</div>

<div id="calltips" class="section">

### <a href="#toc-entry-51" class="toc-backref">Calltips</a>

A handy tooltip is shown when typing ( after a symbol name when the symbol has a parameter list. The tag parser for the filetype must support parsing parameter lists. Calltips can also be shown with a <a href="#editor-keybindings" class="reference external">keybinding</a>.

When there is more than one matching symbol, arrows are shown which can be clicked to cycle through the signatures.

</div>

<div id="user-definable-snippets" class="section">

### <a href="#toc-entry-52" class="toc-backref">User-definable snippets</a>

Snippets are small strings or code constructs which can be replaced or completed to a more complex string. So you can save a lot of time when typing common strings and letting Geany do the work for you. To know what to complete or replace Geany reads a configuration file called snippets.conf at startup.

Maybe you need to often type your name, so define a snippet like this:

``` literal-block
[Default]
myname=Enrico Tröger
```

Every time you write myname \<TAB\> in Geany, it will replace "myname" with "Enrico Tröger". The key to start autocompletion can be changed in the preferences dialog, by default it is TAB. The corresponding keybinding is called Complete snippet.

**Paths**

You can override the default snippets using the user snippets.conf file. Use the *Tools-\>Configuration Files-\>snippets.conf* menu item. See also <a href="#configuration-file-paths" class="reference internal">Configuration file paths</a>.

This adds the default settings to the user file if the file doesn't exist. Alternatively the file can be created manually, adding only the settings you want to change. All missing settings will be read from the system snippets file.

**Snippet groups**

The file snippets.conf contains sections defining snippets that are available for particular filetypes and in general.

The two sections "Default" and "Special" apply to all filetypes. "Default" contains all snippets which are available for every filetype and "Special" contains snippets which can only be used in other snippets. So you can define often used parts of snippets and just use the special snippet as a placeholder (see the snippets.conf for details).

You can define sections with the name of a filetype eg "C++". The snippets in that section are only available for use in files with that filetype. Snippets in filetype sections will hide snippets with the same name in the "Default" section when used in a file of that filetype.

**Substitution sequences for snippets**

To define snippets you can use several special character sequences which will be replaced when using the snippet:

|                  |                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \\n or %newline% | Insert a new line (it will be replaced by the used EOL char(s): LF, CR/LF, or CR).                                                                                                                                               |
| \\t or %ws%      | Insert an indentation step, it will be replaced according to the current document's indent mode.                                                                                                                                 |
| \\s              | \\s to force whitespace at beginning or end of a value ('key= value' won't work, use 'key=\\svalue')                                                                                                                             |
| %cursor%         | Place the cursor at this position after completion has been done. You can define multiple %cursor% wildcards and use the keybinding Move cursor in snippet to jump to the next defined cursor position in the completed snippet. |
| %...%            | "..." means the name of a key in the "Special" section. If you have defined a key "brace_open" in the "Special" section you can use %brace_open% in any other snippet.                                                           |

Snippet names must not contain spaces otherwise they won't work correctly. But beside that you can define almost any string as a snippet and use it later in Geany. It is not limited to existing constructs of certain programming languages(like if, for, switch). Define whatever you need.

**Template wildcards**

Since Geany 0.15 you can also use most of the available templates wildcards listed in <a href="#template-wildcards" class="reference internal">Template wildcards</a>. All wildcards which are listed as available in snippets can be used. For instance to improve the above example:

``` literal-block
[Default]
myname=My name is {developer}
mysystem=My system: {command:uname -a}
```

this will replace myname with "My name is " and the value of the template preference developer.

**Word characters**

You can change the way Geany recognizes the word to complete, that is how the start and end of a word is recognised when the snippet completion is requested. The section "Special" may contain a key "wordchars" which lists all characters a string may contain to be recognized as a word for completion. Leave it commented to use default characters or define it to add or remove characters to fit your needs.

<div id="snippet-keybindings" class="section">

#### <a href="#toc-entry-53" class="toc-backref">Snippet keybindings</a>

Normally you would type the snippet name and press Tab. However, you can define keybindings for snippets under the *Keybindings* group in snippets.conf:

``` literal-block
[Keybindings]
for=<Ctrl>7
block_cursor=<Ctrl>8
```

<div class="admonition note">

Note

Snippet keybindings may be overridden by Geany's configurable keybindings.

</div>

</div>

</div>

<div id="inserting-unicode-characters" class="section">

### <a href="#toc-entry-54" class="toc-backref">Inserting Unicode characters</a>

You can insert Unicode code points by hitting Ctrl-Shift-u, then still holding Ctrl-Shift, type some hex digits representing the code point for the character you want and hit Enter or Return (still holding Ctrl-Shift). If you release Ctrl-Shift before hitting Enter or Return (or any other character), the code insertion is completed, but the typed character is also entered. In the case of Enter/Return, it is a newline, as you might expect.

In some earlier versions of Geany, you might need to first unbind Ctrl-Shift-u in the <a href="#keybinding-preferences" class="reference internal">keybinding preferences</a>, then select *Tools-\>Reload Configuration* or restart Geany. Note that it works slightly differently from other GTK applications, in that you'll need to continue to hold down the Ctrl and Shift keys while typing the code point hex digits (and the Enter or Return to finish the code point).

</div>

<div id="inserting-color-values" class="section">

### <a href="#toc-entry-55" class="toc-backref">Inserting color values</a>

You can insert a color value by selecting *Tools-\>Color Chooser* from the menu. A dialog appears to select the wanted color. If the cursor is placed inside a *\#RRGGBB* format color value then the dialog will show that color after opening. On clicking on *Apply* or *Select* the code for the chosen color will be inserted in the format *\#RRGGBB*. If text is selected, then it will be replaced with the color code on the first click on *Apply* or *Select*. If no text is selected or on subsequent clicks the color code is inserted at the current cursor position.

</div>

</div>

<div id="search-replace-and-go-to" class="section">

## <a href="#toc-entry-56" class="toc-backref">Search, replace and go to</a>

This section describes search-related commands from the Search menu and the editor window's popup menu:

-   Find
-   Find selection
-   Find usage
-   Find in files
-   Replace
-   Go to symbol definition
-   Go to symbol declaration
-   Go to line

See also <a href="#search" class="reference internal">Search</a> preferences.

<div id="toolbar-entries" class="section">

### <a href="#toc-entry-57" class="toc-backref">Toolbar entries</a>

There are also two toolbar entries:

-   Search bar
-   Go to line entry

There are keybindings to focus each of these - see <a href="#focus-keybindings" class="reference internal">Focus keybindings</a>. Pressing Escape will then focus the editor.

<div id="search-bar" class="section">

#### <a href="#toc-entry-58" class="toc-backref">Search bar</a>

The quickest way to find some text is to use the search bar entry in the toolbar. This performs a case-insensitive search in the current document whilst you type. Pressing Enter will search again, and pressing Shift-Enter will search backwards.

</div>

</div>

<div id="find" class="section">

### <a href="#toc-entry-59" class="toc-backref">Find</a>

The Find dialog is used for finding text in one or more open documents.

![](./images/find_dialog.png)

<div id="matching-options" class="section">

#### <a href="#toc-entry-60" class="toc-backref">Matching options</a>

The syntax for the *Use regular expressions* option is shown in <a href="#regular-expressions" class="reference internal">Regular expressions</a>.

<div class="admonition note">

Note

*Use escape sequences* is implied for regular expressions.

</div>

The *Use multi-line matching* option enables multi-line regular expressions instead of single-line ones. See <a href="#regular-expressions" class="reference internal">Regular expressions</a> for more details on the differences between the two modes.

The *Use escape sequences* option will transform any escaped characters into their UTF-8 equivalent. For example, \\t will be transformed into a tab character. Other recognized symbols are: \\\\, \\n, \\r, \\uXXXX (Unicode characters).

</div>

<div id="find-all" class="section">

#### <a href="#toc-entry-61" class="toc-backref">Find all</a>

To find all matches, click on the Find All expander. This will reveal several options:

-   In Document
-   In Session
-   Mark

Find All In Document will show a list of matching lines in the current document in the Messages tab of the Message Window. *Find All In Session* does the same for all open documents.

Mark will highlight all matches in the current document with a colored box. These markers can be removed by selecting the Remove Markers command from the Document menu.

</div>

<div id="change-font-in-search-dialog-text-fields" class="section">

#### <a href="#toc-entry-62" class="toc-backref">Change font in search dialog text fields</a>

All search related dialogs use a Monospace font for the text input fields to increase the readability of input text. This is useful when you are typing input such as regular expressions with spaces, periods and commas which might be hard to read with a proportional font.

If you want to change the font, you can do this easily by using the following custom CSS snippet, see <a href="#customizing-geany-s-appearance-using-gtk-css" class="reference internal">Customizing Geany's appearance using GTK+ CSS</a>:

``` literal-block
#GeanyDialogSearch entry {
    font: 8pt monospace;
}
```

</div>

</div>

<div id="find-selection" class="section">

### <a href="#toc-entry-63" class="toc-backref">Find selection</a>

The *Find Next/Previous Selection* commands perform a search for the current selected text. If nothing is selected, by default the current word is used instead. This can be customized by the *find_selection_type* preference - see <a href="#various-preferences" class="reference internal">Various preferences</a>.

| Value | *find_selection_type* behaviour               |
|-------|-----------------------------------------------|
| 0     | Use the current word (default).               |
| 1     | Try the X selection first, then current word. |
| 2     | Repeat last search.                           |

</div>

<div id="find-usage" class="section">

### <a href="#toc-entry-64" class="toc-backref">Find usage</a>

*Find Usage* searches all open files. It is similar to the *Find All In Session* option in the Find dialog.

If there is a selection, then it is used as the search text; otherwise the current word is used. The current word is either taken from the word nearest the edit cursor, or the word underneath the popup menu click position when the popup menu is used. The search results are shown in the Messages tab of the Message Window.

<div class="admonition note">

Note

You can also use Find Usage for symbol list items from the popup menu.

</div>

</div>

<div id="find-in-files" class="section">

### <a href="#toc-entry-65" class="toc-backref">Find in files</a>

*Find in Files* is a more powerful version of *Find Usage* that searches all files in a certain directory using the Grep tool. The Grep tool must be correctly set in Preferences to the path of the system's Grep utility. GNU Grep is recommended (see note below).

![](./images/find_in_files_dialog.png)

The *Search* field is initially set to the current word in the editor (depending on <a href="#search" class="reference internal">Search</a> preferences).

The *Files* setting allows to choose which files are included in the search, depending on the mode:

All  
Search in all files;

Project  
Use the current project's patterns, see <a href="#project-properties" class="reference internal">Project properties</a>;

Custom  
Use custom patterns.

Both project and custom patterns use a glob-style syntax, each pattern separated by a space. To search all .c and .h files, use: \*.c \*.h. Note that an empty pattern list searches in all files rather than none.

The *Directory* field is initially set to the current document's directory, unless this field has already been edited and the current document has not changed. Otherwise, the current document's directory is prepended to the drop-down history. This can be disabled - see <a href="#search" class="reference internal">Search</a> preferences.

The *Encoding* field can be used to define the encoding of the files to be searched. The entered search text is converted to the chosen encoding and the search results are converted back to UTF-8.

The *Extra options* field is used to pass any additional arguments to the grep tool.

<div class="admonition note">

Note

The *Files* setting uses <span class="pre">--include=</span> when searching recursively, *Recurse in subfolders* uses <span class="pre">-r</span>; both are GNU Grep options and may not work with other Grep implementations.

</div>

<div id="filtering-out-version-control-files" class="section">

#### <a href="#toc-entry-66" class="toc-backref">Filtering out version control files</a>

When using the *Recurse in subfolders* option with a directory that's under version control, you can set the *Extra options* field to filter out version control files.

If you have GNU Grep \>= 2.5.2 you can use the <span class="pre">--exclude-dir</span> argument to filter out CVS and hidden directories like .svn.

Example: <span class="pre">--exclude-dir=.svn</span> <span class="pre">--exclude-dir=CVS</span>

If you have an older Grep, you can try using the <span class="pre">--exclude</span> flag to filter out filenames.

SVN Example: <span class="pre">--exclude=\*.svn-base</span>

The --exclude argument only matches the file name part, not the path.

</div>

</div>

<div id="replace" class="section">

### <a href="#toc-entry-67" class="toc-backref">Replace</a>

The Replace dialog is used for replacing text in one or more open documents.

![](./images/replace_dialog.png)

The Replace dialog has the same options for matching text as the Find dialog. See the section <a href="#matching-options" class="reference internal">Matching options</a>.

The *Use regular expressions* option allows regular expressions to be used in the search string and back references in the replacement text -- see the entry for '\\n' in <a href="#regular-expressions" class="reference internal">Regular expressions</a>.

<div id="replace-all" class="section">

#### <a href="#toc-entry-68" class="toc-backref">Replace all</a>

To replace several matches, click on the *Replace All* expander. This will reveal several options:

-   In Document
-   In Session
-   In Selection

*Replace All In Document* will replace all matching text in the current document. *Replace All In Session* does the same for all open documents. *Replace All In Selection* will replace all matching text in the current selection of the current document.

</div>

</div>

<div id="go-to-symbol-definition" class="section">

### <a href="#toc-entry-69" class="toc-backref">Go to symbol definition</a>

If the current word or selection is the name of a symbol definition (e.g. a function name) and the file containing the symbol definition is open, this command will switch to that file and go to the corresponding line number. The current word is either the word nearest the edit cursor, or the word underneath the popup menu click position when the popup menu is used.

If there are more symbols with the same name to which the goto can be performed, a pop up is shown with a list of all the occurrences. After selecting a symbol from the list Geany jumps to the corresponding symbol location. Geany tries to suggest the nearest symbol (symbol from the current file, other open documents or current directory) as the best candidate for the goto and places this symbol at the beginning of the list typed in boldface.

<div class="admonition note">

Note

If the corresponding symbol is on the current line, Geany will first look for a symbol declaration instead, as this is more useful. Likewise *Go to symbol declaration* will search for a symbol definition first in this case also.

</div>

</div>

<div id="go-to-symbol-declaration" class="section">

### <a href="#toc-entry-70" class="toc-backref">Go to symbol declaration</a>

Like *Go to symbol definition*, but for a forward declaration such as a C function prototype or extern declaration instead of a function body.

</div>

<div id="go-to-line" class="section">

### <a href="#toc-entry-71" class="toc-backref">Go to line</a>

Go to a particular line number in the current file.

If the given value starts with a plus or minus, the value will be interpreted as an offset from the current line.

</div>

<div id="regular-expressions" class="section">

### <a href="#toc-entry-72" class="toc-backref">Regular expressions</a>

You can use regular expressions in the Find and Replace dialogs by selecting the *Use regular expressions* check box (see <a href="#matching-options" class="reference internal">Matching options</a>). The syntax is Perl compatible. Basic syntax is described in the table below. For full details, see <a href="https://www.geany.org/manual/gtk/glib/glib-regex-syntax.html" class="reference external">https://www.geany.org/manual/gtk/glib/glib-regex-syntax.html</a>.

By default regular expressions are matched on a line-by-line basis. If you are interested in multi-line regular expressions, matched against the whole buffer at once, see the section <a href="#multi-line-regular-expressions" class="reference internal">Multi-line regular expressions</a> below.

<div class="admonition note">

Note

1.  The *Use escape sequences* dialog option always applies for regular expressions.
2.  Searching backwards with regular expressions is not supported.
3.  The *Use multi-line matching* dialog option to select single or multi-line matching.

</div>

**In a regular expression, the following characters are interpreted:**

<table class="docutils" data-border="1">
<colgroup>
<col style="width: 10%" />
<col style="width: 90%" />
</colgroup>
<tbody data-valign="top">
<tr class="odd">
<td>.</td>
<td>Matches any character.</td>
</tr>
<tr class="even">
<td>(</td>
<td>This marks the start of a region for tagging a match.</td>
</tr>
<tr class="odd">
<td>)</td>
<td>This marks the end of a tagged region.</td>
</tr>
<tr class="even">
<td>\n</td>
<td><p>Where n is 1 through 9 refers to the first through ninth tagged region when searching or replacing.</p>
<p>Searching for (Wiki)\1 matches WikiWiki.</p>
<p>If the search string was Fred([1-9])XXX and the replace string was Sam\1YYY, when applied to Fred2XXX this would generate Sam2YYY.</p></td>
</tr>
<tr class="odd">
<td>\0</td>
<td>When replacing, the whole matching text.</td>
</tr>
<tr class="even">
<td>\b</td>
<td>This matches a word boundary.</td>
</tr>
<tr class="odd">
<td>\c</td>
<td><p>A backslash followed by d, D, s, S, w or W, becomes a character class (both inside and outside sets []).</p>
<ul>
<li>d: decimal digits</li>
<li>D: any char except decimal digits</li>
<li>s: whitespace (space, \t \n \r \f \v)</li>
<li>S: any char except whitespace (see above)</li>
<li>w: alphanumeric &amp; underscore</li>
<li>W: any char except alphanumeric &amp; underscore</li>
</ul></td>
</tr>
<tr class="even">
<td>\x</td>
<td>This allows you to use a character x that would otherwise have a special meaning. For example, \[ would be interpreted as [ and not as the start of a character set. Use \\ for a literal backslash.</td>
</tr>
<tr class="odd">
<td>[...]</td>
<td><p>Matches one of the characters in the set. If the first character in the set is ^, it matches the characters NOT in the set, i.e. complements the set. A shorthand S-E (start dash end) is used to specify a set of characters S up to E, inclusive.</p>
<p>The special characters ] and - have no special meaning if they appear first in the set. - can also be last in the set. To include both, put ] first: []A-Z-].</p>
<p>Examples:</p>
<pre class="last literal-block"><code>[]|-]    matches these 3 chars
[]-|]    matches from ] to | chars
[a-z]    any lowercase alpha
[^]-]    any char except - and ]
[^A-Z]   any char except uppercase alpha
[a-zA-Z] any alpha</code></pre></td>
</tr>
<tr class="even">
<td>^</td>
<td>This matches the start of a line (unless used inside a set, see above).</td>
</tr>
<tr class="odd">
<td>$</td>
<td>This matches the end of a line.</td>
</tr>
<tr class="even">
<td>*</td>
<td>This matches 0 or more times. For example, Sa*m matches Sm, Sam, Saam, Saaam and so on.</td>
</tr>
<tr class="odd">
<td>+</td>
<td>This matches 1 or more times. For example, Sa+m matches Sam, Saam, Saaam and so on.</td>
</tr>
<tr class="even">
<td>?</td>
<td>This matches 0 or 1 time(s). For example, Joh?n matches John, Jon.</td>
</tr>
</tbody>
</table>

<div class="admonition note">

Note

This table is adapted from Scintilla and SciTE documentation, distributed under the <a href="#license-for-scintilla-and-scite" class="reference internal">License for Scintilla and SciTE</a>.

</div>

<div id="multi-line-regular-expressions" class="section">

#### <a href="#toc-entry-73" class="toc-backref">Multi-line regular expressions</a>

<div class="admonition note">

Note

The *Use multi-line matching* dialog option enables multi-line regular expressions.

</div>

Multi-line regular expressions work just like single-line ones but a match can span several lines.

While the syntax is the same, a few practical differences applies:

|          |                                                                                                                                                                                                                                                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .        | Matches any character but newlines. This behavior can be changed to also match newlines using the (?s) option, see <a href="https://www.geany.org/manual/gtk/glib/glib-regex-syntax.html#idp5671632" class="reference external">https://www.geany.org/manual/gtk/glib/glib-regex-syntax.html#idp5671632</a>                   |
| \[^...\] | A negative range (see above) *will* match newlines if they are not explicitly listed in that negative range. For example, range \[^a-z\] will match newlines, while range \[^a-z\\r\\n\] won't. While this is the expected behavior, it can lead to tricky problems if one doesn't think about it when writing an expression. |

</div>

</div>

</div>

<div id="view-menu" class="section">

## <a href="#toc-entry-74" class="toc-backref">View menu</a>

The View menu allows various elements of the main window to be shown or hidden, and also provides various display-related editor options.

<div id="color-schemes-dialog" class="section">

### <a href="#toc-entry-75" class="toc-backref">Color schemes dialog</a>

The Color Schemes dialog is available under the *View-\>Change Color Scheme* menu item. It lists various color schemes for editor highlighting styles, including the default scheme first. Other items are available based on what color scheme files Geany found at startup.

Color scheme files are read from the <a href="#configuration-file-paths" class="reference internal">Configuration file paths</a> under the colorschemes subdirectory. They should have the extension .conf. The default color scheme is read from filetypes.common.

The <a href="#named-styles-section" class="reference internal">[named_styles] section</a> and <a href="#named-colors-section" class="reference internal">[named_colors] section</a> are the same as for filetypes.common.

The \[theme_info\] section can contain information about the theme. The name and description keys are read to set the menu item text and tooltip, respectively. These keys can have translations, e.g.:

``` literal-block
key=Hello
key[de]=Hallo
key[fr_FR]=Bonjour
```

</div>

</div>

<div id="symbols-and-tags-files" class="section">

## <a href="#toc-entry-76" class="toc-backref">Symbols and tags files</a>

Upon opening, files of supported filetypes are parsed to extract the symbol information (aka "workspace symbols"). You can also have Geany automatically load external files containing the symbol information (aka "global tags files") upon startup, or manually using *Tools --\> Load Tags File*.

Geany uses its own tags file format, similar to what ctags uses (but is incompatible with ctags). You use Geany to generate global tags files, as described below.

<div id="workspace-symbols" class="section">

### <a href="#toc-entry-77" class="toc-backref">Workspace symbols</a>

Each document is parsed for symbols whenever a file is loaded, saved or modified (see *Symbol list update frequency* preference in the <a href="#editor-completions-preferences" class="reference internal">Editor Completions preferences</a>). These are shown in the Symbol list in the Sidebar. These symbols are also used for autocompletion and calltips for all documents open in the current session that have the same filetype.

The *Go to Symbol* commands can be used with all workspace symbols. See <a href="#go-to-symbol-definition" class="reference internal">Go to symbol definition</a>.

</div>

<div id="global-tags-files" class="section">

### <a href="#toc-entry-78" class="toc-backref">Global tags files</a>

Global tags files are used to provide symbols for autocompletion and calltips without having to open the source files containing these symbols. This is intended for library APIs, as the tags file only has to be updated when you upgrade the library.

You can load a custom global tags file in two ways:

-   Using the *Load Tags File* command in the Tools menu.
-   By moving or symlinking tags files to the tags subdirectory of one of the <a href="#configuration-file-paths" class="reference internal">configuration file paths</a> before starting Geany.

You can either download these files or generate your own. They have the format:

``` literal-block
name.lang_ext.tags
```

*lang_ext* is one of the extensions set for the filetype associated with the tags parser. See the section called <a href="#filetype-extensions" class="reference internal">Filetype extensions</a> for more information.

<div id="default-global-tags-files" class="section">

#### <a href="#toc-entry-79" class="toc-backref">Default global tags files</a>

Some global tags files are distributed with Geany and will be loaded automatically when the corresponding filetype is first used. Currently this includes global tags files for these languages:

-   C
-   Pascal
-   PHP
-   HTML -- &symbol; completion, e.g. for ampersand, copyright, etc.
-   LaTeX
-   Python

</div>

<div id="global-tags-file-format" class="section">

#### <a href="#toc-entry-80" class="toc-backref">Global tags file format</a>

Global tags files can have three different formats:

-   CTags format
-   Pipe-separated format
-   Tagmanager format

Tag files using the CTags format should be left unmodified in the form generated by the ctags command-line tool.

For the pipe-separated or tagmanager format, the first line of global tag files should be a comment, introduced by \# followed by a space and format=pipe or format=tagmanager, respectively; these are case-sensitive. This helps Geany to read the file properly. If this line is missing, Geany tries to auto-detect the format used but this might fail.

<div id="ctags-format" class="section">

##### <a href="#toc-entry-81" class="toc-backref">CTags format</a>

This is the recommended tags file format, generated by the ctags command-line tool from the universal-ctags project (<a href="https://github.com/universal-ctags/ctags" class="reference external">https://github.com/universal-ctags/ctags</a>). This format is compatible with the format historically used by Vi.

The format is described at <a href="https://ctags.sourceforge.net/FORMAT" class="reference external">https://ctags.sourceforge.net/FORMAT</a>, but for the full list of existing extensions please refer to universal-ctags. However, note that Geany may actually only honor a subset of the existing extensions.

</div>

<div id="pipe-separated-format" class="section">

##### <a href="#toc-entry-82" class="toc-backref">Pipe-separated format</a>

The Pipe-separated format is easier to read and write. There is one symbol per line and different symbol attributes are separated by the pipe character (\|). A line looks like:

``` literal-block
basename|string|(string path [, string suffix])|
```

<div class="line">

The first field is the symbol name (usually a function name).

</div>

<div class="line">

The second field is the type of the return value.

</div>

<div class="line">

The third field is the argument list for this symbol.

</div>

<div class="line">

The fourth field is the description for this symbol but currently unused and should be left empty.

</div>

</div>

Except for the first field (symbol name), all other field can be left empty but the pipe separator must appear for them.

You can easily write your own global tags files using this format. Just save them in your tags directory, as described earlier in the section <a href="#global-tags-files" class="reference internal">Global tags files</a>.

</div>

<div id="tagmanager-format" class="section">

##### <a href="#toc-entry-83" class="toc-backref">Tagmanager format</a>

The Tagmanager format is a bit more complex and is used for files created by the geany <span class="pre">-g</span> command. There is one symbol per line. Different symbol attributes like the return value or the argument list are separated with different characters indicating the type of the following argument.

</div>

</div>

<div id="generating-a-global-tags-file" class="section">

#### <a href="#toc-entry-84" class="toc-backref">Generating a global tags file</a>

<div id="generating-tags-files-using-ctags" class="section">

##### <a href="#toc-entry-85" class="toc-backref">Generating tags files using ctags</a>

This is currently the recommended way of generating tags files. Unlike the methods below which use the Geany binary for their generation, this method should produce tags files which are compatible across Geany releases, starting from Geany 2.0.

Geany supports loading tag files generated using the ctags command-line tool from the universal-ctags project (<a href="https://github.com/universal-ctags/ctags" class="reference external">https://github.com/universal-ctags/ctags</a>). Even though Geany should work with any ctags file, it is recommended to use certain fields to give Geany some additional information. The recommended fields are EfiklsZSt, so to generate symbols for all sources in the my_project directory one can use:

``` literal-block
ctags -n --fields=EfiklsZSt -R -o my_project.c.tags my_project
```

Additional options may be given to the ctags tool, for instance, to restrict the generated tags file to some languages only, use certain tag kinds, etc.

Note that when the l field (specifying the programming language) is enabled, the language of all symbols is set based on the value of this field instead of the language specified in the extension of the tags file. You however still have to name the file according to the same rules regardless of whether the l field is used or not.

</div>

<div id="generating-tags-files-using-geany" class="section">

##### <a href="#toc-entry-86" class="toc-backref">Generating tags files using Geany</a>

You can generate your own global tags files by parsing a list of source files. The command is:

``` literal-block
geany -g [-P] <Tags File> <File list>
```

-   Tags File filename should be in the format described earlier -- see the section called <a href="#global-tags-files" class="reference internal">Global tags files</a>.
-   File list is a list of filenames, each with a full path (unless you are generating C/C++ tags files and have set the CFLAGS environment variable appropriately).
-   <span class="pre">-P</span> or <span class="pre">--no-preprocessing</span> disables using the C pre-processor to process \#include directives for C/C++ source files. Use this option if you want to specify each source file on the command-line instead of using a 'master' header file. Also can be useful if you don't want to specify the CFLAGS environment variable.

Example for the wxD library for the D programming language:

``` literal-block
geany -g wxd.d.tags /home/username/wxd/wx/*.d
```

</div>

<div id="generating-c-c-tags-files-using-geany" class="section">

##### <a href="#toc-entry-87" class="toc-backref">Generating C/C++ tags files using Geany</a>

You may need to first setup the <a href="#c-ignore-tags" class="reference internal">C ignore.tags</a> file.

For C/C++ tags files gcc is required by default, so that header files can be preprocessed to include any other headers they depend upon. If you do not want this, use the <span class="pre">-P</span> option described above.

For preprocessing, the environment variable CFLAGS should be set with appropriate <span class="pre">-I/path</span> include paths. The following example works with the bash shell, generating a tags file for the GnomeUI library:

``` literal-block
CFLAGS=`pkg-config --cflags libgnomeui-2.0` geany -g gnomeui.c.tags \
/usr/include/libgnomeui-2.0/gnome.h
```

You can adapt this command to use CFLAGS and header files appropriate for whichever libraries you want.

</div>

<div id="generating-tags-files-on-windows-using-geany" class="section">

##### <a href="#toc-entry-88" class="toc-backref">Generating tags files on Windows using Geany</a>

This works basically the same as on other platforms:

``` literal-block
"c:\program files\geany\bin\geany" -g c:\mytags.php.tags c:\code\somefile.php
```

</div>

</div>

</div>

<div id="c-ignore-tags" class="section">

### <a href="#toc-entry-89" class="toc-backref">C ignore.tags</a>

You can ignore certain symbols for C-based languages if they would lead to wrong parsing of the code. Use the *Tools-\>Configuration Files-\>ignore.tags* menu item to open the user ignore.tags file. See also <a href="#configuration-file-paths" class="reference internal">Configuration file paths</a>.

List all symbol names you want to ignore in this file, separated by spaces and/or newlines.

Example:

``` literal-block
G_GNUC_NULL_TERMINATED
G_GNUC_PRINTF
G_GNUC_WARN_UNUSED_RESULT
BAR
```

This will ignore the above macros and will correctly detect 'Foo' as a type instead of 'BAR' in the following code:

struct Foo BAR { int i; };

In addition, it is possible to specify macro definition similarly to the gcc '-D' option:

> \<macro\>=\<definition\> Defines a C preprocessor \<macro\>. This emulates the behavior of the corresponding gcc option. All types of macros are supported, including the ones with parameters and variable arguments. Stringification, token pasting and recursive macro expansion are also supported.

For even more detailed information please read the manual page of Universal Ctags.

</div>

</div>

<div id="preferences" class="section">

## <a href="#toc-entry-90" class="toc-backref">Preferences</a>

You may adjust Geany's settings using the Edit --\> Preferences dialog. Any changes you make there can be applied by hitting either the Apply or the OK button. These settings will persist between Geany sessions. Note that most settings here have descriptive popup bubble help -- just hover the mouse over the item in question to get help on it.

You may also adjust some View settings (under the View menu) that persist between Geany sessions. The settings under the Document menu, however, are only for the current document and revert to defaults when restarting Geany.

<div class="admonition note">

Note

In the paragraphs that follow, the text describing a dialog tab comes after the screenshot of that tab.

</div>

<div id="general-startup-preferences" class="section">

### <a href="#toc-entry-91" class="toc-backref">General Startup preferences</a>

![](./images/pref_dialog_gen_startup.png)

<div id="startup-1" class="section">

#### <a href="#toc-entry-92" class="toc-backref">Startup</a>

Load files from the last session  
On startup, load the same files you had open the last time you used Geany.

Load virtual terminal support  
Load the library for running a terminal in the message window area.

Enable plugin support  
Allow plugins to be used in Geany.

</div>

<div id="shutdown" class="section">

#### <a href="#toc-entry-93" class="toc-backref">Shutdown</a>

Save window position and geometry  
Save the current position and size of the main window so next time you open Geany it's in the same location.

Confirm Exit  
Have a dialog pop up to confirm that you really want to quit Geany.

</div>

<div id="paths" class="section">

#### <a href="#toc-entry-94" class="toc-backref">Paths</a>

Startup path  
Path to start in when opening or saving files. It must be an absolute path.

Project files  
Path to start in when opening project files.

Extra plugin path  
By default Geany looks in the system installation and the user configuration - see <a href="#plugins" class="reference internal">Plugins</a>. In addition the path entered here will be searched. Usually you do not need to set an additional path to search for plugins. It might be useful when Geany is installed on a multi-user machine and additional plugins are available in a common location for all users. Leave blank to not set an additional lookup path.

</div>

</div>

<div id="general-miscellaneous-preferences" class="section">

### <a href="#toc-entry-95" class="toc-backref">General Miscellaneous preferences</a>

![](./images/pref_dialog_gen_misc.png)

<div id="miscellaneous" class="section">

#### <a href="#toc-entry-96" class="toc-backref">Miscellaneous</a>

Beep on errors when compilation has finished  
Have the computer make a beeping sound when compilation of your program has completed or any errors occurred.

Switch status message list at new message  
Switch to the status message tab (in the notebook window at the bottom) once a new status message arrives.

Suppress status messages in the status bar  
Remove all messages from the status bar. The messages are still displayed in the status messages window.

<div class="admonition tip last">

Tip

Another option is to use the *Switch to Editor* keybinding - it reshows the document statistics on the status bar. See <a href="#focus-keybindings" class="reference internal">Focus keybindings</a>.

</div>

Auto-focus widgets (focus follows mouse)  
Give the focus automatically to widgets below the mouse cursor. This works for the main editor widget, the scribble, the toolbar search field go to line fields and the VTE.

</div>

<div id="search" class="section">

#### <a href="#toc-entry-97" class="toc-backref">Search</a>

Always wrap search  
Always wrap search around the document when finding a match.

Hide the Find dialog  
Hide the <a href="#find" class="reference internal">Find</a> dialog after clicking Find Next/Previous.

Use the current word under the cursor for Find dialogs  
Use current word under the cursor when opening the Find, Find in Files or Replace dialog and there is no selection. When this option is disabled, the search term last used in the appropriate Find dialog is used.

Use the current file's directory for Find in Files  
When opening the Find in Files dialog, set the directory to search to the directory of the current active file. When this option is disabled, the directory of the last use of the Find in Files dialog is used. See <a href="#find-in-files" class="reference internal">Find in Files</a> for details.

</div>

<div id="projects" class="section">

#### <a href="#toc-entry-98" class="toc-backref">Projects</a>

Use project-based session files  
Save your current session when closing projects. You will be able to resume different project sessions, automatically opening the files you had open previously.

Store project file inside the project base directory  
When creating new projects, the default path for the project file contains the project base path. Without this option enabled, the default project file path is one level above the project base path. In either case, you can easily set the final project file path in the *New Project* dialog. This option provides the more common defaults automatically for convenience.

</div>

</div>

<div id="interface-preferences" class="section">

### <a href="#toc-entry-99" class="toc-backref">Interface preferences</a>

![](./images/pref_dialog_interface_interface.png)

<div id="sidebar" class="section">

#### <a href="#toc-entry-100" class="toc-backref">Sidebar</a>

Show sidebar  
Whether to show the sidebar at all.

Show symbol list  
Show the list of functions, variables, and other information in the current document you are editing.

Show documents list  
Show all the documents you have open currently. This can be used to change between documents (see <a href="#switching-between-documents" class="reference internal">Switching between documents</a>) and to perform some common operations such as saving, closing and reloading.

Position  
Whether to place the sidebar on the left or right of the editor window.

</div>

<div id="message-window" class="section">

#### <a href="#toc-entry-101" class="toc-backref">Message window</a>

Position  
Whether to place the message window on the bottom or right of the editor window.

</div>

<div id="fonts" class="section">

#### <a href="#toc-entry-102" class="toc-backref">Fonts</a>

Editor  
Change the font used to display documents.

Symbol list  
Change the font used for the Symbols sidebar tab.

Message window  
Change the font used for the message window area.

</div>

<div id="miscellaneous-1" class="section">

#### <a href="#toc-entry-103" class="toc-backref">Miscellaneous</a>

Show status bar  
Show the status bar at the bottom of the main window. It gives information about the file you are editing like the line and column you are on, whether any modifications were done, the file encoding, the filetype and other information.

</div>

</div>

<div id="interface-notebook-tab-preferences" class="section">

### <a href="#toc-entry-104" class="toc-backref">Interface Notebook tab preferences</a>

![](./images/pref_dialog_interface_notebook.png)

<div id="editor-tabs" class="section">

#### <a href="#toc-entry-105" class="toc-backref">Editor tabs</a>

Show editor tabs  
Show a notebook tab for all documents so you can switch between them using the mouse (instead of using the Documents window).

Show close buttons  
Make each tab show a close button so you can easily close open documents.

Placement of new file tabs  
Whether to create a document with its notebook tab to the left or right of all existing tabs.

Next to current  
Whether to place file tabs next to the current tab rather than at the edges of the notebook.

Double-clicking hides all additional widgets  
Whether to call the View-\>Toggle All Additional Widgets command when double-clicking on a notebook tab.

Tab label length  
If filenames are long, set the number of characters that should be visible on each tab's label.

</div>

<div id="tab-positions" class="section">

#### <a href="#toc-entry-106" class="toc-backref">Tab positions</a>

Editor  
Set the positioning of the editor's notebook tabs to the right, left, top, or bottom of the editing window.

Sidebar  
Set the positioning of the sidebar's notebook tabs to the right, left, top, or bottom of the sidebar window.

Message window  
Set the positioning of the message window's notebook tabs to the right, left, top, or bottom of the message window.

</div>

</div>

<div id="interface-toolbar-preferences" class="section">

### <a href="#toc-entry-107" class="toc-backref">Interface Toolbar preferences</a>

Affects the main toolbar underneath the menu bar.

![](./images/pref_dialog_interface_toolbar.png)

<div id="toolbar" class="section">

#### <a href="#toc-entry-108" class="toc-backref">Toolbar</a>

Show Toolbar  
Whether to show the toolbar.

Append Toolbar to the Menu  
Allows to append the toolbar to the main menu bar instead of placing it below. This is useful to save vertical space.

Customize Toolbar  
See <a href="#customizing-the-toolbar" class="reference internal">Customizing the toolbar</a>.

</div>

<div id="appearance" class="section">

#### <a href="#toc-entry-109" class="toc-backref">Appearance</a>

Icon Style  
Select the toolbar icon style to use - either icons and text, just icons or just text. The choice System default uses whatever icon style is set by GTK.

Icon size  
Select the size of the icons you see (large, small or very small). The choice System default uses whatever icon size is set by GTK.

</div>

</div>

<div id="editor-features-preferences" class="section">

### <a href="#toc-entry-110" class="toc-backref">Editor Features preferences</a>

![](./images/pref_dialog_edit_features.png)

<div id="features" class="section">

#### <a href="#toc-entry-111" class="toc-backref">Features</a>

Line wrapping  
Show long lines wrapped around to new display lines.

<!-- -->

"Smart" home key  
Whether to move the cursor to the first non-whitespace character on the line when you hit the home key on your keyboard. Pressing it again will go to the very start of the line.

Disable Drag and Drop  
Do not allow the dragging and dropping of selected text in documents.

Code folding  
Allow groups of lines in a document to be collapsed for easier navigation/editing.

Fold/Unfold all children of a fold point  
Whether to fold/unfold all child fold points when a parent line is folded.

Use indicators to show compile errors  
Underline lines with compile errors using red squiggles to indicate them in the editor area.

Newline strips trailing spaces  
Remove any whitespace at the end of the line when you hit the Enter/Return key. See also <a href="#strip-trailing-spaces" class="reference internal">Strip trailing spaces</a>. Note auto indentation is calculated before stripping, so although this setting will clear a blank line, it will not set the next line indentation back to zero.

Line breaking column  
The editor column number to insert a newline at when Line Breaking is enabled for the current document.

Comment toggle marker  
A string which is added when toggling a line comment in a source file. It is used to mark the comment as toggled.

</div>

</div>

<div id="editor-indentation-preferences" class="section">

### <a href="#toc-entry-112" class="toc-backref">Editor Indentation preferences</a>

![](./images/pref_dialog_edit_indentation.png)

<div id="indentation-group" class="section">

#### <a href="#toc-entry-113" class="toc-backref">Indentation group</a>

See <a href="#indentation" class="reference internal">Indentation</a> for more information.

Width  
The width of a single indent size in spaces. By default the indent size is equivalent to 4 spaces.

Detect width from file  
Try to detect and set the indent width based on file content, when a file is opened.

Type  
When Geany inserts indentation, whether to use:

-   Just Tabs
-   Just Spaces
-   Tabs and Spaces, depending on how much indentation is on a line

The *Tabs and Spaces* indent type is also known as *Soft tab support* in some other editors.

Detect type from file  
Try to detect and set the indent type based on file content, when a file is opened.

Auto-indent mode  
The type of auto-indentation you wish to use after pressing Enter, if any.

Basic  
Just add the indentation of the previous line.

Current chars  
Add indentation based on the current filetype and any characters at the end of the line such as {, } for C, : for Python.

Match braces  
Like *Current chars* but for C-like languages, make a closing } brace line up with the matching opening brace.

Tab key indents  
If set, pressing tab will indent the current line or selection, and unindent when pressing Shift-tab. Otherwise, the tab key will insert a tab character into the document (which can be different from indentation, depending on the indent type).

<div class="admonition note last">

Note

There are also separate configurable keybindings for indent & unindent, but this preference allows the tab key to have different meanings in different contexts - e.g. for snippet completion.

</div>

Backspace key unindents  
If set, pressing backspace while the cursor is in leading whitespace will reduce the indentation level, unless the indentation mode is tabs. Otherwise, the backspace key will delete the character before the cursor.

</div>

</div>

<div id="editor-completions-preferences" class="section">

### <a href="#toc-entry-114" class="toc-backref">Editor Completions preferences</a>

![](./images/pref_dialog_edit_completions.png)

<div id="completions" class="section">

#### <a href="#toc-entry-115" class="toc-backref">Completions</a>

Snippet Completion  
Whether to replace special keywords after typing Tab into a pre-defined text snippet. See <a href="#user-definable-snippets" class="reference internal">User-definable snippets</a>.

XML/HTML tag auto-closing  
When you open an XML/HTML tag automatically generate its completion tag.

Automatic continuation multi-line comments  
Continue automatically multi-line comments in languages like C, C++ and Java when a new line is entered inside such a comment. With this option enabled, Geany will insert a \* on every new line inside a multi-line comment, for example when you press return in the following C code:

``` literal-block
/*
 * This is a C multi-line comment, press <Return>
```

then Geany would insert:

``` literal-block
*
```

on the next line with the correct indentation based on the previous line, as long as the multi-line is not closed by \*/. If the previous line has no \* prefix, no \* will be added to the new line.

Autocomplete symbols  
When you start to type a symbol name, look for the full string to allow it to be completed for you.

Autocomplete all words in document  
When you start to type a word, Geany will search the whole document for words starting with the typed part to complete it, assuming there are no symbol names to show.

Drop rest of word on completion  
Remove any word part to the right of the cursor when choosing a completion list item.

Characters to type for autocompletion  
Number of characters of a word to type before autocompletion is displayed.

Completion list height  
The number of rows to display for the autocompletion window.

Max. symbol name suggestions  
The maximum number of items in the autocompletion list.

Symbol list update frequency  
The minimum delay (in milliseconds) between two symbol list updates.

This option determines how frequently the symbol list is updated for the current document. The smaller the delay, the more up-to-date the symbol list (and then the completions); but rebuilding the symbol list has a cost in performance, especially with large files.

The default value is 250ms, which means the symbol list will be updated at most four times per second, even if the document changes continuously.

A value of 0 disables automatic updates, so the symbol list will only be updated upon document saving.

</div>

<div id="auto-close-quotes-and-brackets" class="section">

#### <a href="#toc-entry-116" class="toc-backref">Auto-close quotes and brackets</a>

Geany can automatically insert a closing bracket and quote characters when you open them. For instance, you type a ( and Geany will automatically insert ). With the following options, you can define for which characters this should work.

Parenthesis ( )  
Auto-close parenthesis when typing an opening one

Curly brackets { }  
Auto-close curly brackets (braces) when typing an opening one

Square brackets \[ \]  
Auto-close square brackets when typing an opening one

Single quotes ' '  
Auto-close single quotes when typing an opening one

Double quotes " "  
Auto-close double quotes when typing an opening one

</div>

</div>

<div id="editor-display-preferences" class="section">

### <a href="#toc-entry-117" class="toc-backref">Editor Display preferences</a>

This is for visual elements displayed in the editor window.

![](./images/pref_dialog_edit_display.png)

<div id="display" class="section">

#### <a href="#toc-entry-118" class="toc-backref">Display</a>

Invert syntax highlighting colors  
Invert all colors, by default this makes white text on a black background.

Show indentation guides  
Show vertical lines to help show how much leading indentation there is on each line.

Show whitespaces  
Mark all tabs with an arrow "--\>" symbol and spaces with dots to show which kinds of whitespace are used.

Show line endings  
Display a symbol everywhere that a carriage return or line feed is present.

Show only non-default line endings  
Shows line ending characters only when they differ from the file default line ending character.

Show line numbers  
Show or hide the Line Number margin.

Show markers margin  
Show or hide the small margin right of the line numbers, which is used to mark lines.

Stop scrolling at last line  
When enabled Geany stops scrolling when at the last line of the document. Otherwise you can scroll one more page even if there are no real lines.

Lines visible around the cursor  
The number of lines to maintain between the cursor and the top and bottom edges of the view. This allows some lines of context around the cursor to always be visible. If *Stop scrolling at last line* is disabled, the cursor will never reach the bottom edge when this value is greater than 0.

</div>

<div id="long-line-marker" class="section">

#### <a href="#toc-entry-119" class="toc-backref">Long line marker</a>

The long line marker helps to indicate overly-long lines, or as a hint to the user for when to break the line.

Type  
Line  
Show a thin vertical line in the editor window at the given column position.

Background  
Change the background color of characters after the given column position to the color set below. (This is recommended over the *Line* setting if you use proportional fonts).

Disabled  
Don't mark long lines at all.

Long line marker  
Set this value to a value greater than zero to specify the column where it should appear.

Long line marker color  
Set the color of the long line marker.

</div>

<div id="virtual-spaces" class="section">

#### <a href="#toc-entry-120" class="toc-backref">Virtual spaces</a>

Virtual space is space beyond the end of each line. The cursor may be moved into virtual space but no real space will be added to the document until there is some text typed or some other text insertion command is used.

Disabled  
Do not show virtual spaces

Only for rectangular selections  
Only show virtual spaces beyond the end of lines when drawing a rectangular selection

Always  
Always show virtual spaces beyond the end of lines

</div>

<div id="change-history" class="section">

#### <a href="#toc-entry-121" class="toc-backref">Change History</a>

The *change history* feature enables changed text in a document to be shown in the markers margin or by underlining the text. By default, the *change history* feature is disabled.

Newly added, modified and removed lines or words are highlighted to easily track changes to the opened document. The changes can be shown as vertical bars in the markers margin and/or as underlines in the text directly.

<div class="admonition note">

Note

This feature may use a moderate amount of memory, especially if there are many or big changes in the document. Also, modification information is not kept when re-opening a document - all change markers will be lost.

</div>

![](./images/edit_change_history.png)

The image shows the default visuals:

-   inserted characters appear with coloured underlines
-   points where characters were deleted are shown with small triangles
-   the margin shows a block indicating the overall state of the line, prioritizing the more consequential modified states
-   the states are modified (orange), saved (green), saved then reverted to modified (green-yellow), and saved then reverted to original (cyan).

Show in markers margin  
Changes are shown in the markers margin as vertical bars

Show as underline indicators  
Changes are shown as underlines in the text directly

</div>

</div>

<div id="files-preferences" class="section">

### <a href="#toc-entry-122" class="toc-backref">Files preferences</a>

![](./images/pref_dialog_files.png)

<div id="new-files" class="section">

#### <a href="#toc-entry-123" class="toc-backref">New files</a>

Open new documents from the command-line  
Whether to create new documents when passing filenames that don't exist from the command-line.

Default encoding (new files)  
The type of file encoding you wish to use when creating files.

Default encoding (existing files)  
Selects the encoding used when opening existing files. If set to something other than *Detect from file*, all files will be opened with the specified encoding instead of auto-detecting it. Use a specific encoding when it's not possible for Geany to detect the correct one.

Default end of line characters  
The end of line characters to which should be used for new files. On Windows systems, you generally want to use CR/LF which are the common characters to mark line breaks. On Unix-like systems, LF is default and CR is used on MAC systems.

</div>

<div id="saving-files" class="section">

#### <a href="#toc-entry-124" class="toc-backref">Saving files</a>

Perform formatting operations when a document is saved. These can each be undone with the Undo command.

Ensure newline at file end  
Add a newline at the end of the document if one is missing.

Ensure consistent line endings  
Ensures that newline characters always get converted before saving, avoiding mixed line endings in the same file.

<!-- -->

Strip trailing spaces  
Remove any whitespace at the end of each document line.

<div class="admonition note last">

Note

This does not apply to Diff documents, e.g. patch files.

</div>

Replace tabs with spaces  
Replace all tabs in the document with the equivalent number of spaces.

<div class="admonition note last">

Note

It is better to use spaces to indent than use this preference - see <a href="#indentation" class="reference internal">Indentation</a>.

</div>

</div>

<div id="miscellaneous-2" class="section">

#### <a href="#toc-entry-125" class="toc-backref">Miscellaneous</a>

Recent files list length  
The number of files to remember in the recently used files list.

Disk check timeout  
The number of seconds to periodically check the current document's file on disk in case it has changed. Setting it to 0 will disable this feature.

<div class="admonition note last">

Note

These checks are only performed on local files. Remote files are not checked for changes due to performance issues (remote files are files in <span class="pre">\~/.gvfs/</span>).

</div>

</div>

</div>

<div id="tools-preferences" class="section">

### <a href="#toc-entry-126" class="toc-backref">Tools preferences</a>

![](./images/pref_dialog_tools.png)

<div id="tool-paths" class="section">

#### <a href="#toc-entry-127" class="toc-backref">Tool paths</a>

Terminal  
The command to execute a script in a terminal. Occurrences of %c in the command are substituted with the run script name, see <a href="#terminal-emulators" class="reference internal">Terminal emulators</a>.

Browser  
The location of your web browser executable.

Grep  
The location of the grep executable.

<div class="admonition note">

Note

For Windows users: at the time of writing it is recommended to use the grep.exe from the UnxUtils project (<a href="https://sourceforge.net/projects/unxutils" class="reference external">https://sourceforge.net/projects/unxutils</a>). The grep.exe from the Mingw project for instance might not work with Geany at the moment.

</div>

</div>

<div id="commands" class="section">

#### <a href="#toc-entry-128" class="toc-backref">Commands</a>

Context action  
Set this to a command to execute on the current word. You can use the "%s" wildcard to pass the current word below the cursor to the specified command.

</div>

</div>

<div id="template-preferences" class="section">

### <a href="#toc-entry-129" class="toc-backref">Template preferences</a>

See <a href="#templates" class="reference internal">Templates</a>.

This data is used as meta data for various template text to insert into a document, such as the file header. You only need to set fields that you want to use in your template files.

![](./images/pref_dialog_templ.png)

<div id="template-data" class="section">

#### <a href="#toc-entry-130" class="toc-backref">Template data</a>

See <a href="#template-meta-data" class="reference internal">Template meta data</a>.

Developer  
The name of the developer who will be creating files.

Initials  
The initials of the developer.

Mail address  
The email address of the developer.

<div class="admonition note last">

Note

You may wish to add anti-spam markup, e.g. name\<at\>site\<dot\>ext.

</div>

Company  
The company the developer is working for.

Initial version  
The initial version of files you will be creating.

Year  
Specify a format for the {year} wildcard.

Date  
Specify a format for the {date} wildcard.

Date & Time  
Specify a format for the {datetime} wildcard.

See <a href="#date-time-wildcards" class="reference internal">Date &amp; time wildcards</a> for more information.

</div>

</div>

<div id="keybinding-preferences" class="section">

### <a href="#toc-entry-131" class="toc-backref">Keybinding preferences</a>

![](./images/pref_dialog_keys.png)

There are some commands listed in the keybinding dialog that are not, by default, bound to a key combination, and may not be available as a menu item.

<div class="admonition note">

Note

For more information see the section <a href="#keybindings" class="reference internal">Keybindings</a>.

</div>

</div>

<div id="printing-preferences" class="section">

### <a href="#toc-entry-132" class="toc-backref">Printing preferences</a>

![](./images/pref_dialog_printing.png)

Use external command for printing  
Use a system command to print your file out.

Use native GTK printing  
Let the GTK GUI toolkit handle your print request.

Print line numbers  
Print the line numbers on the left of your paper.

Print page number  
Print the page number on the bottom right of your paper.

Print page header  
Print a header on every page that is sent to the printer.

Use base name of the printed file  
Don't use the entire path for the header, only the filename.

Date format  
How the date should be printed. For a list of available conversion specifiers see <a href="https://docs.gtk.org/glib/method.DateTime.format.html" class="reference external">https://docs.gtk.org/glib/method.DateTime.format.html</a>.

</div>

<div id="various-preferences" class="section">

### <a href="#toc-entry-133" class="toc-backref">Various preferences</a>

![](./images/pref_dialog_various.png)

Rarely used preferences, explained in the table below. A few of them require restart to take effect, and a few other will only affect newly opened or created documents before restart.

| Key                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Default    | Applies          |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|------------------|
| **\`\`editor\`\` group**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |            |                  |
| use_gtk_word_boundaries                  | Whether to look for the end of a word when using word-boundary related Scintilla commands (see <a href="#scintilla-keyboard-commands" class="reference internal">Scintilla keyboard commands</a>).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | true       | to new documents |
| brace_match_ltgt                         | Whether to highlight \<, \> angle brackets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | false      | immediately      |
| complete_snippets_whilst_editing         | Whether to allow completion of snippets when editing an existing line (i.e. there is some text after the current cursor position on the line). Only used when the keybinding Complete snippet is set to Space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | false      | immediately      |
| show_editor_scrollbars                   | Whether to display scrollbars. If set to false, the horizontal and vertical scrollbars are hidden completely.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | true       | immediately      |
| indent_hard_tab_width                    | The size of a tab character. Don't change it unless you really need to; use the indentation settings instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 8          | immediately      |
| editor_ime_interaction                   | Input method editor (IME)'s candidate window behaviour. May be 0 (windowed) or 1 (inline)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0          | to new documents |
| **\`\`interface\`\` group**              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |            |                  |
| show_symbol_list_expanders               | Whether to show or hide the small expander icons on the symbol list treeview.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | true       | to new documents |
| compiler_tab_autoscroll                  | Whether to automatically scroll to the last line of the output in the Compiler tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | true       | immediately      |
| statusbar_template                       | The status bar statistics line format. (See <a href="#statusbar-templates" class="reference internal">Statusbar Templates</a> for details).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | See below. | immediately      |
| new_document_after_close                 | Whether to open a new document after all documents have been closed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | false      | immediately      |
| msgwin_status_visible                    | Whether to show the Status tab in the Messages Window                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | true       | immediately      |
| msgwin_compiler_visible                  | Whether to show the Compiler tab in the Messages Window                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | true       | immediately      |
| msgwin_messages_visible                  | Whether to show the Messages tab in the Messages Window                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | true       | immediately      |
| msgwin_scribble_visible                  | Whether to show the Scribble tab in the Messages Window                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | true       | immediately      |
| warn_on_project_close                    | Whether to show a warning when opening a project while one is already open.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | true       | immediately      |
| **\`\`terminal\`\` group**               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |            |                  |
| send_selection_unsafe                    | By default, Geany strips any trailing newline characters from the current selection before sending it to the terminal to not execute arbitrary code. This is mainly a security feature. If, for whatever reasons, you really want it to be executed directly, set this option to true.                                                                                                                                                                                                                                                                                                                                                                                                   | false      | immediately      |
| send_cmd_prefix                          | String with which prefix the commands sent to the shell. This may be used to tell some shells (BASH with HISTCONTROL set to ignorespace, ZSH with HIST_IGNORE_SPACE enabled, etc.) from putting these commands in their history by setting this to a space. Note that leading spaces must be escaped using s in the configuration file.                                                                                                                                                                                                                                                                                                                                                  | Empty      | immediately      |
| **\`\`files\`\` group**                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |            |                  |
| allow_always_save                        | Whether files can be saved always, even if they don't have any changes. By default, the Save button and menu item are disabled when a file is unchanged. When setting this option to true, the Save button and menu item are always active and files can be saved.                                                                                                                                                                                                                                                                                                                                                                                                                       | false      | immediately      |
| use_atomic_file_saving                   | Defines the mode how Geany saves files to disk. If disabled, Geany directly writes the content of the document to disk. This might cause loss of data when there is no more free space on disk to save the file. When set to true, Geany first saves the contents into a temporary file and if this succeeded, the temporary file is moved to the real file to save. This gives better error checking in case of no more free disk space. But it also destroys hard links of the original file and its permissions (e.g. executable flags are reset). Use this with care as it can break things seriously. The better approach would be to ensure your disk won't run out of free space. | false      | immediately      |
| use_gio_unsafe_file_saving               | Whether to use GIO as the unsafe file saving backend. It is better on most situations but is known not to work correctly on some complex setups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | true       | immediately      |
| gio_unsafe_save_backup                   | Make a backup when using GIO unsafe file saving. Backup is named filename\~.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | false      | immediately      |
| keep_edit_history_on_reload              | Whether to maintain the edit history when reloading a file, and allow the operation to be reverted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | true       | immediately      |
| show_keep_edit_history_on_reload_msg     | Whether to show a confirmation dialog to drop the edit history on reloading a file, see also keep_edit_history_on_reload above.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | true       | immediately      |
| reload_clean_doc_on_file_change          | Whether to automatically reload documents that have no changes but which have changed on disk. If unsaved changes exist then the user is prompted to reload manually.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | false      | immediately      |
| save_config_on_file_change               | Automatically save Geany's configuration to disk once the document list changes (i.e. new documents are opened, saved or closed). This helps to prevent accidentally losing the session file list or other changed settings when Geany is not shut down cleanly. Disable this option if your configuration directory is on a slow drive, network share or similar and you experience problems.                                                                                                                                                                                                                                                                                           | true       | immediately      |
| extract_filetype_regex                   | Regex to extract filetype name from file via capture group one. See <a href="#ft-regex" class="reference internal">ft_regex</a> for default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | See link   | immediately      |
| **\`\`search\`\` group**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |            |                  |
| find_selection_type                      | See <a href="#find-selection" class="reference internal">Find selection</a>.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0          | immediately      |
| replace_and_find_by_default              | Set Replace & Find button as default so it will be activated when the Enter key is pressed while one of the text fields has focus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | true       | immediately      |
| skip_confirmation_for_replace_in_session | If set, do *not* show the confirmation dialog before replacing text in the whole session, i.e. in all open files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | false      | immediately      |
| **\`\`build\`\` group**                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |            |                  |
| number_ft_menu_items                     | The maximum number of menu items in the filetype build section of the Build menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 2          | on restart       |
| number_non_ft_menu_items                 | The maximum number of menu items in the independent build section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 3          | on restart       |
| number_exec_menu_items                   | The maximum number of menu items in the execute section of the Build menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 2          | on restart       |
| **\`\`socket\`\` group**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |            |                  |
| socket_remote_cmd_port                   | TCP port number to be used for inter process communication (i.e. with other Geany instances, e.g. "Open with Geany"). Only available on Windows, valid port range: 1024 to 65535.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 2          | on restart       |

<div id="statusbar-templates" class="section">

#### <a href="#toc-entry-134" class="toc-backref">Statusbar Templates</a>

The default statusbar template is (note \\t = tab):

line: %l / %L\\t col: %c\\t sel: %s\\t %w      %t      %mEOL: %M      encoding: %e      filetype: %f      scope: %S

Settings the preference to an empty string will also cause Geany to use this internal default.

The following format characters are available for the statusbar template:

| Placeholder | Description                                                                                                                    |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|
| %l          | The current line number starting at 1                                                                                          |
| %L          | The total number of lines                                                                                                      |
| %c          | The current column number starting at 0, including virtual space.                                                              |
| %C          | The current column number starting at 1, including virtual space.                                                              |
| %s          | The number of selected characters or if only whole lines selected, the number of selected lines.                               |
| %n          | The number of selected characters, even if only whole lines are selected.                                                      |
| %w          | Shows RO when the document is in read-only mode, otherwise shows whether the editor is in overtype (OVR) or insert (INS) mode. |
| %t          | Shows the indentation mode, either tabs (TAB), spaces (SP) or both (T/S).                                                      |
| %m          | Shows whether the document is modified (MOD) or nothing.                                                                       |
| %M          | The name of the document's line-endings (ex. Unix (LF))                                                                        |
| %e          | The name of the document's encoding (ex. UTF-8).                                                                               |
| %f          | The filetype of the document (ex. None, Python, C, etc).                                                                       |
| %S          | The name of the scope where the caret is located.                                                                              |
| %p          | The caret position in the entire document starting at 0.                                                                       |
| %r          | Shows whether the document is read-only (RO) or nothing.                                                                       |
| %Y          | The Scintilla style number at the caret position. This is useful if you're debugging color schemes or related code.            |

</div>

</div>

<div id="terminal-vte-preferences" class="section">

### <a href="#toc-entry-135" class="toc-backref">Terminal (VTE) preferences</a>

See also: <a href="#virtual-terminal-emulator-widget-vte" class="reference internal">Virtual terminal emulator widget (VTE)</a>.

![](./images/pref_dialog_vte.png)

<div id="terminal-widget" class="section">

#### <a href="#toc-entry-136" class="toc-backref">Terminal widget</a>

Terminal font  
Select the font that will be used in the terminal emulation control.

Foreground color  
Select the font color.

Background color  
Select the background color of the terminal.

Background image  
Select the background image to show behind the terminal's text.

Scrollback lines  
The number of lines buffered so that you can scroll though the history.

Shell  
The location of the shell on your system.

Scroll on keystroke  
Scroll the terminal to the prompt line when pressing a key.

Scroll on output  
Scroll the output down.

Cursor blinks  
Let the terminal cursor blink.

Override Geany keybindings  
Allow the VTE to receive keyboard shortcuts (apart from focus commands).

Disable menu shortcut key (F10 by default)  
Disable the menu shortcut when you are in the virtual terminal.

Follow path of the current file  
Make the path of the terminal change according to the path of the current file.

Execute programs in VTE  
Execute programs in the virtual terminal instead of using the external terminal tool. Note that if you run multiple execute commands at once the output may become mixed together in the VTE.

Don't use run script  
Don't use the simple run script which is usually used to display the exit status of the executed program. This can be useful if you already have a program running in the VTE like a Python console (e.g. ipython). Use this with care.

</div>

</div>

</div>

<div id="project-management" class="section">

## <a href="#toc-entry-137" class="toc-backref">Project management</a>

Project management is optional in Geany. Currently it can be used for:

-   Storing and opening session files on a project basis.
-   Overriding default settings with project equivalents.
-   Configuring the Build menu on a project basis.

A list of session files can be stored and opened with the project when the *Use project-based session files* preference is enabled, in the <a href="#projects" class="reference internal">Projects</a> group of the <a href="#general-miscellaneous-preferences" class="reference internal">General Miscellaneous preferences</a> tab of the <a href="#preferences" class="reference internal">Preferences</a> dialog.

As long as a project is open, the Build menu will use the items defined in project's settings, instead of the defaults. See <a href="#build-menu-configuration" class="reference internal">Build Menu Configuration</a> for information on configuring the menu.

The current project's settings are saved when it is closed, or when Geany is shutdown. When restarting Geany, the previously opened project file that was in use at the end of the last session will be reopened.

The project menu items are detailed below.

<div id="new-project" class="section">

### <a href="#toc-entry-138" class="toc-backref">New project</a>

There are two ways of creating new projects, either by using *Project-\>New* menu item or by using *Project-\>New from Folder* menu item.

New  
This method is more suitable for creating new, empty projects from scratch at the default location without having any existing sources.

To create a new project, fill in the *Name* field. By default this will setup a new project file \~/projects/name/name.geany.

The *Base path* text field is setup to use \~/projects/name. This can safely be set to any existing path -- it will not touch the file structure contained in it.

New from Folder  
This method is more suitable when there is already some folder containing source files for which you want to create a new project.

When using this method, Geany first opens a directory selection dialog to select the folder containing the sources, and the *Base path* field is set to that value.

Afterwards, Geany shows the same dialog as the *Project-\>New* method but already pre-filled with the values based on the *Base path* selection. The *Name* field is filled with the folder name, the *Filename* field is filled with base_path/name.geany and the *Base path* field is filled with the path specified in the previous dialog.

</div>

<div id="project-properties" class="section">

### <a href="#toc-entry-139" class="toc-backref">Project properties</a>

You can set an optional description for the project. Currently it's only used for the {description}} template wildcard - see <a href="#dynamic-wildcards" class="reference internal">Dynamic wildcards</a>.

The *Base path* field is used as the directory to run the Build menu commands. The specified path can be an absolute path or it is considered to be relative to the project's file name.

The *File patterns* field allows to specify a list of file patterns for the project, which can be used in the <a href="#find-in-files" class="reference internal">Find in files</a> dialog.

The *Indentation* tab allows you to override the default <a href="#indentation" class="reference internal">Indentation</a> settings.

</div>

<div id="open-project" class="section">

### <a href="#toc-entry-140" class="toc-backref">Open project</a>

The Open command displays a standard file chooser, starting in \~/projects. Choose a project file named with the .geany extension.

When project session support is enabled, Geany will close the currently open files and open the session files associated with the project.

</div>

<div id="close-project" class="section">

### <a href="#toc-entry-141" class="toc-backref">Close project</a>

Project file settings are saved when the project is closed.

When project session support is enabled, Geany will close the project session files and open any previously closed default session files.

</div>

</div>

<div id="build-menu" class="section">

## <a href="#toc-entry-142" class="toc-backref">Build menu</a>

After editing code with Geany, the next step is to compile, link, build, interpret, run etc. As Geany supports many languages each with a different approach to such operations, and as there are also many language independent software building systems, Geany does not have a built-in build system, nor does it limit which system you can use. Instead the build menu provides a configurable and flexible means of running any external commands to execute your preferred build system.

This section provides a description of the default configuration of the build menu and then covers how to configure it, and where the defaults fit in.

Running the commands from within Geany has two benefits:

-   The current file is automatically saved before the command is run.
-   The output is captured in the Compiler notebook tab and parsed for warnings or errors.

Warnings and errors that can be parsed for line numbers will be shown in red in the Compiler tab and you can click on them to switch to the relevant source file (or open it) and mark the line number. Also lines with warnings or errors are marked in the source, see <a href="#indicators" class="reference internal">Indicators</a> below.

<div class="admonition tip">

Tip

If Geany's default error message parsing does not parse errors for the tool you're using, you can set a custom regex in the <a href="#set-build-commands-dialog" class="reference internal">Set Build Commands dialog</a>, see <a href="#build-menu-configuration" class="reference internal">Build Menu Configuration</a>.

</div>

<div id="indicators" class="section">

### <a href="#toc-entry-143" class="toc-backref">Indicators</a>

Indicators are red squiggly underlines which are used to highlight errors which occurred while compiling the current file. So you can easily see where your code failed to compile. You can remove them by selecting *Remove Error Indicators* in the Document menu.

If you do not like this feature, you can disable it - see <a href="#editor-features-preferences" class="reference internal">Editor Features preferences</a>.

</div>

<div id="default-build-menu-items" class="section">

### <a href="#toc-entry-144" class="toc-backref">Default build menu items</a>

Depending on the current file's filetype, the default Build menu will contain the following items:

-   Compile
-   Build
-   Lint
-   Make All
-   Make Custom Target
-   Make Object
-   Next Error
-   Previous Error
-   Execute
-   Set Build Menu Commands

<div id="compile" class="section">

#### <a href="#toc-entry-145" class="toc-backref">Compile</a>

The Compile command has different uses for different kinds of files.

For compilable languages such as C and C++, the Compile command is set up to compile the current source file into a binary object file.

Java source files will be compiled to class file bytecode.

Interpreted languages such as Perl, Python, Ruby will compile to bytecode if the language supports it, or will run a syntax check, or if that is not available will run the file in its language interpreter.

</div>

<div id="build" class="section">

#### <a href="#toc-entry-146" class="toc-backref">Build</a>

For compilable languages such as C and C++, the Build command will link the current source file's equivalent object file into an executable. If the object file does not exist, the source will be compiled and linked in one step, producing just the executable binary.

Interpreted languages do not use the Build command.

<div class="admonition note">

Note

If you need complex settings for your build system, or several different settings, then writing a Makefile and using the Make commands is recommended; this will also make it easier for users to build your software.

</div>

</div>

<div id="lint" class="section">

#### <a href="#toc-entry-147" class="toc-backref">Lint</a>

Source code linters are often used to find code that doesn't correspond to certain style guidelines: non-portable code, common or hard to find errors, code "smells", variables used before being set, unused functions, division by zero, constant conditions, etc. Linters inspect the code and issue warnings much like the compilers do. This is formally referred to as static code analysis.

Some common linters are pre-configured for you in the Build menu (pycodestyle for Python, cppcheck for C/C++, JSHint for JavaScript, xmllint for XML, hlint for Haskell, shellcheck for shell code, ...), but all these are standalone tools you need to obtain before using.

</div>

<div id="make" class="section">

#### <a href="#toc-entry-148" class="toc-backref">Make</a>

This runs "make" in the same directory as the current file.

</div>

<div id="make-custom-target" class="section">

#### <a href="#toc-entry-149" class="toc-backref">Make custom target</a>

This is similar to running 'Make' but you will be prompted for the make target name to be passed to the Make tool. For example, typing 'clean' in the dialog prompt will run "make clean".

</div>

<div id="make-object" class="section">

#### <a href="#toc-entry-150" class="toc-backref">Make object</a>

Make object will run "make current_file.o" in the same directory as the current file, using the filename for 'current_file'. It is useful for building just the current file without building the whole project.

</div>

<div id="next-error" class="section">

#### <a href="#toc-entry-151" class="toc-backref">Next error</a>

The next error item will move to the next detected error in the file.

</div>

<div id="previous-error" class="section">

#### <a href="#toc-entry-152" class="toc-backref">Previous error</a>

The previous error item will move to the previous detected error in the file.

</div>

<div id="execute" class="section">

#### <a href="#toc-entry-153" class="toc-backref">Execute</a>

Execute will run the corresponding executable file, shell script or interpreted script in a terminal window. The command set in the <a href="#set-build-commands-dialog" class="reference internal">Set Build Commands dialog</a> is run in a script to ensure the terminal stays open after execution completes. Note: see <a href="#terminal-emulators" class="reference internal">Terminal emulators</a> below for the command format. Alternatively the built-in VTE can be used if it is available - see <a href="#virtual-terminal-emulator-widget-vte" class="reference internal">Virtual terminal emulator widget (VTE)</a>.

After your program or script has finished executing, the run script will prompt you to press the return key. This allows you to review any text output from the program before the terminal window is closed.

<div class="admonition note">

Note

The execute command output is not parsed for errors.

</div>

</div>

<div id="stopping-running-processes" class="section">

#### <a href="#toc-entry-154" class="toc-backref">Stopping running processes</a>

When there is a running program, the Execute menu item in the menu and the Run button in the toolbar each become a stop button so you can stop the current running program (and any child processes). This works by sending the SIGQUIT signal to the process.

Depending on the process you started it is possible that the process cannot be stopped. For example this can happen when the process creates more than one child process.

<div id="terminal-emulators" class="section">

##### <a href="#toc-entry-155" class="toc-backref">Terminal emulators</a>

The Terminal field of the tools preferences tab requires a command to execute the terminal program and to pass it the name of the Geany run script that it should execute in a Bourne compatible shell (eg /bin/sh). The marker "%c" is substituted with the name of the Geany run script, which is created in the temporary directory and which changes the working directory to the directory set in the <a href="#set-build-commands-dialog" class="reference internal">Set Build Commands dialog</a>.

As an example the default (Linux) command is:

``` literal-block
xterm -e "/bin/sh %c"
```

</div>

</div>

<div id="set-build-commands" class="section">

#### <a href="#toc-entry-156" class="toc-backref">Set build commands</a>

By default Compile, Build and Execute are fairly basic commands. You may wish to customise them using *Set Build Commands*.

E.g. for C you can add any include paths and compile flags for the compiler, any library names and paths for the linker, and any arguments you want to use when running Execute.

</div>

</div>

<div id="build-menu-configuration" class="section">

### <a href="#toc-entry-157" class="toc-backref">Build menu configuration</a>

The build menu has considerable flexibility and configurability, allowing menu labels, the commands they execute and the directory they execute in to be configured. For example, if you change one of the default make commands to run say 'waf' you can also change the label to match. These settings are saved automatically when Geany is shut down.

The build menu is divided into four groups of items each with different behaviors:

-   Filetype build commands - are configurable and depend on the filetype of the current document; they capture output in the compiler tab and parse it for errors.
-   Independent build commands - are configurable and mostly don't depend on the filetype of the current document; they also capture output in the compiler tab and parse it for errors.
-   Execute commands - are configurable and intended for executing your program or other long running programs. The output is not parsed for errors and is directed to the terminal command selected in <a href="#tools-preferences" class="reference internal">Tools preferences</a>.
-   Fixed commands - these perform built-in actions:
    -   Go to the next error.
    -   Go to the previous error.
    -   Show the build menu commands dialog.

The maximum numbers of items in each of the configurable groups can be configured in <a href="#various-preferences" class="reference internal">Various preferences</a>. Even though the maximum number of items may have been increased, only those menu items that have commands configured are shown in the menu.

The groups of menu items obtain their configuration from four potential sources. The highest priority source that has the menu item defined will be used. The sources in decreasing priority are:

-   A project file if open
-   The user preferences
-   The system filetype definitions
-   The defaults

The detailed relationships between sources and the configurable menu item groups is shown in the following table:

<table class="docutils" data-border="1">
<colgroup>
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 23%" />
<col style="width: 17%" />
<col style="width: 28%" />
</colgroup>
<thead data-valign="bottom">
<tr class="header">
<th class="head">Group</th>
<th class="head">Project File</th>
<th class="head">Preferences</th>
<th class="head">System Filetype</th>
<th class="head">Defaults</th>
</tr>
</thead>
<tbody data-valign="top">
<tr class="odd">
<td>Filetype Build</td>
<td><p>Loads From: project file</p>
<p>Saves To: project file</p></td>
<td><p>Loads From: filetypes.xxx file in ~/.config/geany/filedefs</p>
<p>Saves to: as above, creating if needed.</p></td>
<td><p>Loads From: filetypes.xxx in Geany install</p>
<p>Saves to: as user preferences left.</p></td>
<td>None</td>
</tr>
<tr class="even">
<td>Independent Build</td>
<td><p>Loads From: project file</p>
<p>Saves To: project file</p></td>
<td><p>Loads From: geany.conf file in ~/.config/geany</p>
<p>Saves to: as above, creating if needed.</p></td>
<td><p>Loads From: filetypes.xxx in Geany install</p>
<p>Saves to: as user preferences left.</p></td>
<td><dl>
<dt>1:</dt>
<dd>
Label: _Make Command: make
</dd>
<dt>2:</dt>
<dd>
Label: Make Custom _Target Command: make
</dd>
<dt>3:</dt>
<dd>
Label: Make _Object Command: make %e.o
</dd>
</dl></td>
</tr>
<tr class="odd">
<td>Execute</td>
<td><p>Loads From: project file or else filetype defined in project file</p>
<p>Saves To: project file</p></td>
<td><p>Loads From: geany.conf file in ~/.config/geany or else filetypes.xxx file in ~/.config/geany/filedefs</p>
<p>Saves To: filetypes.xxx file in ~/.config/geany/filedefs</p></td>
<td><p>Loads From: filetypes.xxx in Geany install</p>
<p>Saves To: as user preferences left.</p></td>
<td>Label: _Execute Command: ./%e</td>
</tr>
</tbody>
</table>

The following notes on the table may reference cells by coordinate as *(group, source)*:

-   Filetype filenames - for filetypes.xxx substitute the appropriate extension for the filetype of the current document for xxx - see <a href="#filenames" class="reference internal">filenames</a>.
-   System Filetypes - Labels loaded from these sources are locale sensitive and can contain translations.
-   *(Filetype build, Project and Preferences)* - preferences use a full filetype file so that users can configure all other filetype preferences as well. Projects can only configure menu items per filetype. Saving in the project file means that there is only one file per project not a whole directory.
-   *(Filetype-Independent build, System Filetype)* - although conceptually strange, defining filetype-independent commands in a filetype file, this provides the ability to define filetype dependent default menu items.
-   *(Execute, Project and Preferences)* - the project independent execute and preferences independent execute commands can only be set by hand editing the appropriate file, see <a href="#preferences-file-format" class="reference internal">Preferences file format</a> and <a href="#project-file-format" class="reference internal">Project file format</a>.

</div>

<div id="set-build-commands-dialog" class="section">

### <a href="#toc-entry-158" class="toc-backref">Set Build Commands dialog</a>

Most of the configuration of the build menu is done through the <a href="#set-build-commands-dialog" class="reference internal">Set Build Commands dialog</a>. When no project is open, you can edit the configuration sourced from user preferences using the *Build-\>Set Build Commands* menu item. You can edit the configuration sourced from a project in the *Build* tab of the <a href="#project-properties" class="reference internal">Project Properties</a> dialog. The former menu item also shows the project dialog when a project is open. Both use the same form shown below.

![](./images/build_menu_commands_dialog.png)

The dialog is divided into three sections:

-   Filetype build commands (selected based on the current document's filetype).
-   Independent build commands (available regardless of filetype).
-   Filetype execute commands.

The filetype and independent build sections also each contain a field for the regular expression used for parsing command output for error and warning messages.

The columns in the first three sections allow setting of the label, command, and working directory to run the command in. An item with an empty label will not be shown in the menu. An empty working directory will default to the directory of the current document.

If there is no current document then the command will not run.

The dialog will always show the command selected by priority, not just the commands configured in this configuration source. This ensures that you always see what the menu item is going to do if activated.

If the current source of the menu item is higher priority than the configuration source you are editing then the command will be shown in the dialog but will be insensitive (greyed out). This can't happen with the project source but can with the preferences source dialog.

The clear buttons remove the definition from the configuration source you are editing. When you do this the command from the next lower priority source will be shown. To hide lower priority menu items without having anything show in the menu, configure with nothing in the label but at least one character in the command.

<div id="substitutions-in-commands-and-working-directories" class="section">

#### <a href="#toc-entry-159" class="toc-backref">Substitutions in commands and working directories</a>

Before the command is run, the first occurrence of each of the following two character sequences in each of the command and working directory fields is substituted by the items specified below:

-   %% - a literal % sign.
-   %d - the absolute path to the directory of the current file.
-   %e - the name of the current file without the extension or path.
-   %f - the name of the current file without the path.
-   %p - if a project is open, the base path from the project.
-   %l - the line number at the current cursor position.

<div class="admonition note">

Note

If the base path set in <a href="#project-properties" class="reference internal">Project Properties</a> is not an absolute path, then it is taken as relative to the directory of the project file. This allows a project file stored in the source tree to specify all commands and working directories relative to the tree itself, so that the whole tree including the project file, can be moved and even checked into and out of version control without having to re-configure the build menu.

</div>

</div>

<div id="build-menu-keyboard-shortcuts" class="section">

#### <a href="#toc-entry-160" class="toc-backref">Build menu keyboard shortcuts</a>

Keyboard shortcuts can be defined for:

-   the first two filetype build menu items
-   the first three independent build menu items
-   the first execute menu item
-   the fixed menu items (Next/Previous Error, Set Commands)

In the keybindings configuration dialog (see <a href="#keybinding-preferences" class="reference internal">Keybinding preferences</a>) these items are identified by the default labels shown in the <a href="#build-menu" class="reference internal">Build Menu</a> section above.

It is currently not possible to bind keyboard shortcuts to more than these menu items. You can also use underlines in the labels to set mnemonic characters.

</div>

<div id="old-settings" class="section">

#### <a href="#toc-entry-161" class="toc-backref">Old settings</a>

The configurable Build Menu capability was introduced in Geany 0.19 and required a new section to be added to the configuration files (See <a href="#preferences-file-format" class="reference internal">Preferences file format</a>). Geany will still load older format project, preferences and filetype file settings and will attempt to map them into the new configuration format. There is not a simple clean mapping between the formats. The mapping used produces the most sensible results for the majority of cases. However, if they do not map the way you want, you may have to manually configure some settings using the <a href="#set-build-commands-dialog" class="reference internal">Set Build Commands dialog</a>.

Any setting configured in either of these dialogs will override settings mapped from older format configuration files.

</div>

</div>

</div>

<div id="printing-support" class="section">

## <a href="#toc-entry-162" class="toc-backref">Printing support</a>

Since Geany 0.13 there has been printing support using GTK's printing API. The printed page(s) will look nearly the same as on your screen in Geany. Additionally, there are some options to modify the printed page(s).

<div class="admonition note">

Note

The background text color is set to white, except for text with a white foreground. This allows dark color schemes to save ink when printing.

</div>

You can define whether to print line numbers, page numbers at the bottom of each page and whether to print a page header on each page. This header contains the filename of the printed document, the current page number and the date and time of printing. By default, the file name of the document with full path information is added to the header. If you prefer to add only the basename of the file(without any path information) you can set it in the preferences dialog. You can also adjust the format of the date and time added to the page header. For a list of available conversion specifiers see <a href="https://docs.gtk.org/glib/method.DateTime.format.html" class="reference external">https://docs.gtk.org/glib/method.DateTime.format.html</a>.

All of these settings can also be changed in the print dialog just before actual printing is done. On Unix-like systems the provided print dialog offers a print preview. The preview file is opened with a PDF viewer and by default GTK uses evince for print preview. If you have not installed evince or just want to use another PDF viewer, you can change the program to use in the file settings.ini (usually found in <span class="pre">\~/.config/gtk-3.0</span>, see the <a href="https://developer.gnome.org/gtk3/stable/GtkSettings.html#GtkSettings.description" class="reference external">GTK documentation</a>). For example, use:

``` literal-block
[Settings]
gtk-print-preview-command = epdfview %f
```

Of course, you can also use xpdf, kpdf or whatever as the print preview command. That command should ideally delete the temporary file referenced by %f. See the <a href="https://developer.gnome.org/gtk3/stable/GtkSettings.html#GtkSettings--gtk-print-preview-command" class="reference external">GTK documentation for the setting</a> for more details.

Geany also provides an alternative basic printing support using a custom print command. However, the printed document contains no syntax highlighting. You can adjust the command to which the filename is passed in the preferences dialog. The default command is:

``` literal-block
% lpr "%d/%f"
```

See <a href="#substitutions-in-commands-and-working-directories" class="reference internal">Substitutions in commands and working directories</a> for available placeholders referencing the current file. Geany will not show errors from the command itself, so you should make sure that it works before (e.g. by trying to execute it from the command line).

A nicer example, which many prefer is:

``` literal-block
% a2ps -1 --medium=A4 -o - "%d/%f" | xfprint4
```

But this depends on a2ps and xfprint4. As a replacement for xfprint4, gtklp or similar programs can be used.

</div>

<div id="plugins" class="section">

## <a href="#toc-entry-163" class="toc-backref">Plugins</a>

Plugins are loaded at startup, if the *Enable plugin support* general preference is set. There is also a command-line option, <span class="pre">-p</span>, which prevents plugins being loaded. Plugins are scanned in the following directories:

-   $prefix/lib/geany on Unix-like systems (see <a href="#installation-prefix" class="reference internal">Installation prefix</a>)
-   The lib subfolder of the installation path on Windows.
-   The plugins subfolder of the user configuration directory - see <a href="#configuration-file-paths" class="reference internal">Configuration file paths</a>.
-   The Extra plugin path preference (usually blank) - see <a href="#paths" class="reference internal">Paths</a>.

Most plugins add menu items to the *Tools* menu when they are loaded.

See also <a href="#plugin-documentation" class="reference internal">Plugin documentation</a> for information about single plugins which are included in Geany.

<div id="plugin-manager" class="section">

### <a href="#toc-entry-164" class="toc-backref">Plugin manager</a>

The Plugin Manager dialog lets you choose which plugins should be loaded at startup. You can also load and unload plugins on the fly using this dialog. Once you click the checkbox for a specific plugin in the dialog, it is loaded or unloaded according to its previous state. By default, no plugins are loaded at startup until you select some. You can also configure some plugin specific options if the plugin provides any.

</div>

</div>

<div id="keybindings" class="section">

## <a href="#toc-entry-165" class="toc-backref">Keybindings</a>

Geany supports the default keyboard shortcuts for the Scintilla editing widget. For a list of these commands, see <a href="#scintilla-keyboard-commands" class="reference internal">Scintilla keyboard commands</a>. The Scintilla keyboard shortcuts will be overridden by any custom keybindings with the same keyboard shortcut.

<div id="switching-documents" class="section">

### <a href="#toc-entry-166" class="toc-backref">Switching documents</a>

There are some non-configurable bindings to switch between documents, listed below. These can also be overridden by custom keybindings.

| Key         | Action                             |
|-------------|------------------------------------|
| Alt-\[1-9\] | Select left-most tab, from 1 to 9. |
| Alt-0       | Select right-most tab.             |

See also <a href="#notebook-tab-keybindings" class="reference internal">Notebook tab keybindings</a>.

</div>

<div id="configurable-keybindings" class="section">

### <a href="#toc-entry-167" class="toc-backref">Configurable keybindings</a>

For all actions listed below you can define your own keybindings. Open the Preferences dialog, select the desired action and click on change. In the resulting dialog you can press the key combination you want to assign to the action and it will be saved when you press OK. You can define only one key combination for each action and each key combination can only be defined for one action.

The following tables list all customizable keyboard shortcuts, those which are common to many applications are marked with (C) after the shortcut.

<div id="file-keybindings" class="section">

#### <a href="#toc-entry-168" class="toc-backref">File keybindings</a>

| Action                  | Default shortcut | Description                                                                                                                                                                                                       |
|-------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| New                     | Ctrl-N (C)       | Creates a new file.                                                                                                                                                                                               |
| Open                    | Ctrl-O (C)       | Opens a file.                                                                                                                                                                                                     |
| Open selected file      | Ctrl-Shift-O     | Opens the selected filename.                                                                                                                                                                                      |
| Re-open last closed tab |                  | Re-opens the last closed document tab.                                                                                                                                                                            |
| Save                    | Ctrl-S (C)       | Saves the current file.                                                                                                                                                                                           |
| Save As                 |                  | Saves the current file under a new name.                                                                                                                                                                          |
| Save all                | Ctrl-Shift-S     | Saves all open files.                                                                                                                                                                                             |
| Close all               | Ctrl-Shift-W     | Closes all open files.                                                                                                                                                                                            |
| Close                   | Ctrl-W (C)       | Closes the current file.                                                                                                                                                                                          |
| Reload file             | Ctrl-R (C)       | Reloads the current file.                                                                                                                                                                                         |
| Reload all              |                  | Reloads all open files. If the reload will not be 'undo'-able and changes that will be lost are detected (unsaved or saved) the reload will be confirmed, otherwise the reload will proceed without confirmation. |
| Print                   | Ctrl-P (C)       | Prints the current file.                                                                                                                                                                                          |
| Quit                    | Ctrl-Q (C)       | Quits Geany.                                                                                                                                                                                                      |

</div>

<div id="editor-keybindings" class="section">

#### <a href="#toc-entry-169" class="toc-backref">Editor keybindings</a>

| Action                      | Default shortcut     | Description                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Undo                        | Ctrl-Z (C)           | Un-does the last action.                                                                                                                                                                                                                                                                                                                                       |
| Redo                        | Ctrl-Y               | Re-does the last action.                                                                                                                                                                                                                                                                                                                                       |
| Delete current line(s)      | Ctrl-K               | Deletes the current line (and any lines with a selection).                                                                                                                                                                                                                                                                                                     |
| Delete to line end          | Ctrl-Shift-Delete    | Deletes from the current caret position to the end of the current line.                                                                                                                                                                                                                                                                                        |
| Delete to line start        | Ctrl-Shift-BackSpace | Deletes from the beginning of the line to the current caret position.                                                                                                                                                                                                                                                                                          |
| Duplicate line or selection | Ctrl-D               | Duplicates the current line or selection.                                                                                                                                                                                                                                                                                                                      |
| Transpose current line      |                      | Transposes the current line with the previous one.                                                                                                                                                                                                                                                                                                             |
| Scroll to current line      | Ctrl-Shift-L         | Scrolls the current line into the centre of the view. The cursor position and or an existing selection will not be changed.                                                                                                                                                                                                                                    |
| Scroll up by one line       | Alt-Up               | Scrolls the view.                                                                                                                                                                                                                                                                                                                                              |
| Scroll down by one line     | Alt-Down             | Scrolls the view.                                                                                                                                                                                                                                                                                                                                              |
| Complete word               | Ctrl-Space           | Shows the autocompletion list. If already showing symbol completion, it shows document word completion instead, even if it is not enabled for automatic completion. Likewise if no symbol suggestions are available, it shows document word completion.                                                                                                        |
| Show calltip                | Ctrl-Shift-Space     | Shows a calltip for the current function or method.                                                                                                                                                                                                                                                                                                            |
| Complete snippet            | Tab                  | If you type a keyword like if or for and press this key, it will be completed with a matching template - see <a href="#user-definable-snippets" class="reference internal">User-definable snippets</a>.                                                                                                                                                        |
| Suppress snippet completion |                      | If you type a construct like if or for and press this key, it will not be completed, and a space or tab will be inserted, depending on what the construct completion keybinding is set to. For example, if you have set the construct completion keybinding to a space, then setting this to Shift+space will prevent construct completion and insert a space. |
| Context Action              |                      | Executes a command and passes the current word (near the cursor position) or selection as an argument. See the section called <a href="#context-actions" class="reference internal">Context actions</a>.                                                                                                                                                       |
| Move cursor in snippet      |                      | Jumps to the next defined cursor positions in a completed snippets if multiple cursor positions where defined.                                                                                                                                                                                                                                                 |
| Word part completion        | Tab                  | When the autocompletion list is visible, complete the currently selected item up to the next word part.                                                                                                                                                                                                                                                        |
| Move line(s) up             | Alt-PageUp           | Move the current line or selected lines up by one line.                                                                                                                                                                                                                                                                                                        |
| Move line(s) down           | Alt-PageDown         | Move the current line or selected lines down by one line.                                                                                                                                                                                                                                                                                                      |

</div>

<div id="clipboard-keybindings" class="section">

#### <a href="#toc-entry-170" class="toc-backref">Clipboard keybindings</a>

| Action               | Default shortcut | Description                                                                |
|----------------------|------------------|----------------------------------------------------------------------------|
| Cut                  | Ctrl-X (C)       | Cut the current selection to the clipboard.                                |
| Copy                 | Ctrl-C (C)       | Copy the current selection to the clipboard.                               |
| Paste                | Ctrl-V (C)       | Paste the clipboard text into the current document.                        |
| Cut current line(s)  | Ctrl-Shift-X     | Cuts the current line (and any lines with a selection) to the clipboard.   |
| Copy current line(s) | Ctrl-Shift-C     | Copies the current line (and any lines with a selection) to the clipboard. |

</div>

<div id="select-keybindings" class="section">

#### <a href="#toc-entry-171" class="toc-backref">Select keybindings</a>

| Action                       | Default shortcut | Description                                                                                   |
|------------------------------|------------------|-----------------------------------------------------------------------------------------------|
| Select all                   | Ctrl-A (C)       | Makes a selection of all text in the current document.                                        |
| Select current word          | Alt-Shift-W      | Selects the current word under the cursor.                                                    |
| Select current paragraph     | Alt-Shift-P      | Selects the current paragraph under the cursor which is defined by two empty lines around it. |
| Select current line(s)       | Alt-Shift-L      | Selects the current line under the cursor (and any partially selected lines).                 |
| Select to previous word part |                  | (Extend) selection to previous word part boundary.                                            |
| Select to next word part     |                  | (Extend) selection to next word part boundary.                                                |

</div>

<div id="insert-keybindings" class="section">

#### <a href="#toc-entry-172" class="toc-backref">Insert keybindings</a>

| Action                         | Default shortcut | Description                                                                                                                                                            |
|--------------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Insert date                    | Shift-Alt-D      | Inserts a customisable date.                                                                                                                                           |
| Insert alternative whitespace  |                  | Inserts a tab character when spaces should be used for indentation and inserts space characters of the amount of a tab width when tabs should be used for indentation. |
| Insert New Line Before Current |                  | Inserts a new line with indentation.                                                                                                                                   |
| Insert New Line After Current  |                  | Inserts a new line with indentation.                                                                                                                                   |

</div>

<div id="format-keybindings" class="section">

#### <a href="#toc-entry-173" class="toc-backref">Format keybindings</a>

| Action                         | Default shortcut | Description                                                                                                                                                                                                                                         |
|--------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Toggle case of selection       | Ctrl-Alt-U       | Changes the case of the selection. A lowercase selection will be changed into uppercase and vice versa. If the selection contains lower- and uppercase characters, all will be converted to lowercase.                                              |
| Comment line                   |                  | Comments current line or selection.                                                                                                                                                                                                                 |
| Uncomment line                 |                  | Uncomments current line or selection.                                                                                                                                                                                                               |
| Toggle line commentation       | Ctrl-E           | Comments a line if it is not commented or removes a comment if the line is commented.                                                                                                                                                               |
| Increase indent                | Ctrl-I           | Indents the current line or selection by one tab or with spaces in the amount of the tab width setting.                                                                                                                                             |
| Decrease indent                | Ctrl-U           | Removes one tab or the amount of spaces of the tab width setting from the indentation of the current line or selection.                                                                                                                             |
| Increase indent by one space   |                  | Indents the current line or selection by one space.                                                                                                                                                                                                 |
| Decrease indent by one space   |                  | Deindents the current line or selection by one space.                                                                                                                                                                                               |
| Smart line indent              |                  | Indents the current line or all selected lines with the same indentation as the previous line.                                                                                                                                                      |
| Send to Custom Command 1 (2,3) | Ctrl-1 (2,3)     | Passes the current selection to a configured external command (available for the first 9 configured commands, see <a href="#sending-text-through-custom-commands" class="reference internal">Sending text through custom commands</a> for details). |
| Send Selection to Terminal     |                  | Sends the current selection or the current line (if there is no selection) to the embedded Terminal (VTE).                                                                                                                                          |
| Reflow lines/block             |                  | Reformat selected lines or current (indented) text block, breaking lines at the long line marker or the line breaking column if line breaking is enabled for the current document.                                                                  |
| Join Lines                     |                  | Replace line endings and following indentation with a single space throughout the selection or current (indented) text block.                                                                                                                       |

</div>

<div id="settings-keybindings" class="section">

#### <a href="#toc-entry-174" class="toc-backref">Settings keybindings</a>

| Action             | Default shortcut | Description                      |
|--------------------|------------------|----------------------------------|
| Preferences        | Ctrl-Alt-P       | Opens preferences dialog.        |
| Plugin Preferences |                  | Opens plugin preferences dialog. |

</div>

<div id="search-keybindings" class="section">

#### <a href="#toc-entry-175" class="toc-backref">Search keybindings</a>

| Action                  | Default shortcut | Description                                                                                                                                                                                                                       |
|-------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Find                    | Ctrl-F (C)       | Opens the Find dialog.                                                                                                                                                                                                            |
| Find Next               | Ctrl-G           | Finds next result.                                                                                                                                                                                                                |
| Find Previous           | Ctrl-Shift-G     | Finds previous result.                                                                                                                                                                                                            |
| Find Next Selection     |                  | Finds next occurrence of selected text.                                                                                                                                                                                           |
| Find Previous Selection |                  | Finds previous occurrence of selected text.                                                                                                                                                                                       |
| Replace                 | Ctrl-H (C)       | Opens the Replace dialog.                                                                                                                                                                                                         |
| Find in files           | Ctrl-Shift-F     | Opens the Find in files dialog.                                                                                                                                                                                                   |
| Next message            |                  | Jumps to the line with the next message in the Messages window.                                                                                                                                                                   |
| Previous message        |                  | Jumps to the line with the previous message in the Messages window.                                                                                                                                                               |
| Find Usage              | Ctrl-Shift-E     | Finds all occurrences of the current word or selection (see note below) in all open documents and displays them in the messages window.                                                                                           |
| Find Document Usage     | Ctrl-Shift-D     | Finds all occurrences of the current word or selection (see note below) in the current document and displays them in the messages window.                                                                                         |
| Mark All                | Ctrl-Shift-M     | Highlight all matches of the current word/selection (see note below) in the current document with a colored box. If there's nothing to find, or the cursor is next to an existing match, the highlighted matches will be cleared. |

<div class="admonition note">

Note

The keybindings marked "see note below" work like this: if no text is selected, the word under cursor is used, and *it has to match fully* (like when Match only a whole word is enabled in the Search dialog). However if some text is selected, then it is matched regardless of word boundaries.

</div>

</div>

<div id="go-to-keybindings" class="section">

#### <a href="#toc-entry-176" class="toc-backref">Go to keybindings</a>

| Action                      | Default shortcut | Description                                                                                                                                                                                                                                                   |
|-----------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Navigate forward a location | Alt-Right (C)    | Switches to the next location in the navigation history. See the section called <a href="#code-navigation-history" class="reference internal">Code Navigation History</a>.                                                                                    |
| Navigate back a location    | Alt-Left (C)     | Switches to the previous location in the navigation history. See the section called <a href="#code-navigation-history" class="reference internal">Code navigation history</a>.                                                                                |
| Go to line                  | Ctrl-L           | Focuses the Go to Line entry (if visible) or shows the Go to line dialog.                                                                                                                                                                                     |
| Go to matching brace        | Ctrl-B           | If the cursor is ahead or behind a brace, then it is moved to the brace which belongs to the current one. If this keyboard shortcut is pressed again, the cursor is moved back to the first brace.                                                            |
| Toggle marker               | Ctrl-M           | Set a marker on the current line, or clear the marker if there already is one.                                                                                                                                                                                |
| Go to next marker           | Ctrl-.           | Go to the next marker in the current document.                                                                                                                                                                                                                |
| Go to previous marker       | Ctrl-,           | Go to the previous marker in the current document.                                                                                                                                                                                                            |
| Go to symbol definition     | Ctrl-T           | Jump to the definition of the current word or selection. See <a href="#go-to-symbol-definition" class="reference internal">Go to symbol definition</a>.                                                                                                       |
| Go to symbol declaration    | Ctrl-Shift-T     | Jump to the declaration of the current word or selection. See <a href="#go-to-symbol-declaration" class="reference internal">Go to symbol declaration</a>.                                                                                                    |
| Go to Start of Line         | Home             | Move the caret to the start of the line. Behaves differently if <a href="#smart-home-key" class="reference internal">smart_home_key</a> is set.                                                                                                               |
| Go to End of Line           | End              | Move the caret to the end of the line.                                                                                                                                                                                                                        |
| Go to Start of Display Line | Alt-Home         | Move the caret to the start of the display line. This is useful when you use line wrapping and want to jump to the start of the wrapped, virtual line, not the real start of the whole line. If the line is not wrapped, it behaves like Go to Start of Line. |
| Go to End of Display Line   | Alt-End          | Move the caret to the end of the display line. If the line is not wrapped, it behaves like Go to End of Line.                                                                                                                                                 |
| Go to Previous Word Part    | Ctrl-/           | Go to the previous part of the current word.                                                                                                                                                                                                                  |
| Go to Next Word Part        | Ctrl-\\          | Go to the next part of the current word.                                                                                                                                                                                                                      |

</div>

<div id="view-keybindings" class="section">

#### <a href="#toc-entry-177" class="toc-backref">View keybindings</a>

| Action                        | Default shortcut | Description                                                                                                       |
|-------------------------------|------------------|-------------------------------------------------------------------------------------------------------------------|
| Fullscreen                    | F11 (C)          | Switches to fullscreen mode.                                                                                      |
| Toggle Messages Window        |                  | Toggles the message window (status and compiler messages) on and off.                                             |
| Toggle Sidebar                |                  | Shows or hides the sidebar.                                                                                       |
| Toggle all additional widgets |                  | Hide and show all additional widgets like the notebook tabs, the toolbar, the messages window and the status bar. |
| Zoom In                       | Ctrl-+ (C)       | Zooms in the text.                                                                                                |
| Zoom Out                      | Ctrl-- (C)       | Zooms out the text.                                                                                               |
| Zoom Reset                    | Ctrl-0           | Reset any previous zoom on the text.                                                                              |

</div>

<div id="focus-keybindings" class="section">

#### <a href="#toc-entry-178" class="toc-backref">Focus keybindings</a>

| Action                          | Default shortcut | Description                                                                                   |
|---------------------------------|------------------|-----------------------------------------------------------------------------------------------|
| Switch to Editor                | F2               | Switches to editor widget. Also reshows the document statistics line (after a short timeout). |
| Switch to Search Bar            | F7               | Switches to the search bar in the toolbar (if visible).                                       |
| Switch to Message Window        |                  | Focus the Message Window's current tab.                                                       |
| Switch to Compiler              |                  | Focus the Compiler message window tab.                                                        |
| Switch to Messages              |                  | Focus the Messages message window tab.                                                        |
| Switch to Scribble              | F6               | Switches to scribble widget.                                                                  |
| Switch to VTE                   | F4               | Switches to VTE widget.                                                                       |
| Switch to Sidebar               |                  | Focus the Sidebar.                                                                            |
| Switch to Sidebar Symbol List   |                  | Focus the Symbol list tab in the Sidebar (if visible).                                        |
| Switch to Sidebar Document List |                  | Focus the Document list tab in the Sidebar (if visible).                                      |

</div>

<div id="notebook-tab-keybindings" class="section">

#### <a href="#toc-entry-179" class="toc-backref">Notebook tab keybindings</a>

| Action                       | Default shortcut    | Description                                                                                                                                                                                                                                                                                                       |
|------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Switch to left document      | Ctrl-PageUp (C)     | Switches to the previous open document.                                                                                                                                                                                                                                                                           |
| Switch to right document     | Ctrl-PageDown (C)   | Switches to the next open document.                                                                                                                                                                                                                                                                               |
| Switch to last used document | Ctrl-Tab            | Switches to the previously shown document (if it's still open). Holding Ctrl (or another modifier if the keybinding has been changed) will show a dialog, then repeated presses of the keybinding will switch to the 2nd-last used document, 3rd-last, etc. Also known as Most-Recently-Used documents switching. |
| Move document left           | Ctrl-Shift-PageUp   | Changes the current document with the left hand one.                                                                                                                                                                                                                                                              |
| Move document right          | Ctrl-Shift-PageDown | Changes the current document with the right hand one.                                                                                                                                                                                                                                                             |
| Move document first          |                     | Moves the current document to the first position.                                                                                                                                                                                                                                                                 |
| Move document last           |                     | Moves the current document to the last position.                                                                                                                                                                                                                                                                  |

</div>

<div id="document-keybindings" class="section">

#### <a href="#toc-entry-180" class="toc-backref">Document keybindings</a>

| Action                              | Default shortcut | Description                                                                                                                |
|-------------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------|
| Clone                               |                  | See <a href="#cloning-documents" class="reference internal">Cloning documents</a>.                                         |
| Replace tabs with space             |                  | Replaces all tabs with the right amount of spaces in the whole document, or the current selection.                         |
| Replace spaces with tabs            |                  | Replaces leading spaces with tab characters in the whole document, or the current selection.                               |
| Toggle current fold                 |                  | Toggles the folding state of the current code block.                                                                       |
| Fold all                            |                  | Folds all contractible code blocks.                                                                                        |
| Unfold all                          |                  | Unfolds all contracted code blocks.                                                                                        |
| Reload symbol list                  | Ctrl-Shift-R     | Reloads the symbol list.                                                                                                   |
| Toggle Line wrapping                |                  | Enables or disables wrapping of long lines.                                                                                |
| Toggle Line breaking                |                  | Enables or disables automatic breaking of long lines at a configurable column.                                             |
| Remove Markers                      |                  | Remove any markers on lines or words which were set by using 'Mark All' in the search dialog or by manually marking lines. |
| Remove Error Indicators             |                  | Remove any error indicators in the current document.                                                                       |
| Remove Markers and Error Indicators |                  | Combines Remove Markers and Remove Error Indicators.                                                                       |

</div>

<div id="project-keybindings" class="section">

#### <a href="#toc-entry-181" class="toc-backref">Project keybindings</a>

| Action     | Default shortcut | Description                |
|------------|------------------|----------------------------|
| New        |                  | Create a new project.      |
| Open       |                  | Opens a project file.      |
| Properties |                  | Shows project properties.  |
| Close      |                  | Close the current project. |

</div>

<div id="build-keybindings" class="section">

#### <a href="#toc-entry-182" class="toc-backref">Build keybindings</a>

| Action             | Default shortcut | Description                                                            |
|--------------------|------------------|------------------------------------------------------------------------|
| Compile            | F8               | Compiles the current file.                                             |
| Build              | F9               | Builds (compiles if necessary and links) the current file.             |
| Make all           | Shift-F9         | Builds the current file with the Make tool.                            |
| Make custom target | Ctrl-Shift-F9    | Builds the current file with the Make tool and a given target.         |
| Make object        | Shift-F8         | Compiles the current file with the Make tool.                          |
| Next error         |                  | Jumps to the line with the next error from the last build process.     |
| Previous error     |                  | Jumps to the line with the previous error from the last build process. |
| Run                | F5               | Executes the current file in a terminal emulation.                     |
| Set Build Commands |                  | Opens the build commands dialog.                                       |

</div>

<div id="tools-keybindings" class="section">

#### <a href="#toc-entry-183" class="toc-backref">Tools keybindings</a>

| Action             | Default shortcut | Description                     |
|--------------------|------------------|---------------------------------|
| Show Color Chooser |                  | Opens the Color Chooser dialog. |

</div>

<div id="help-keybindings" class="section">

#### <a href="#toc-entry-184" class="toc-backref">Help keybindings</a>

| Action | Default shortcut | Description       |
|--------|------------------|-------------------|
| Help   | F1 (C)           | Opens the manual. |

</div>

</div>

</div>

</div>

<div id="configuration-files" class="section">

# <a href="#toc-entry-185" class="toc-backref">Configuration files</a>

<div class="admonition warning">

Warning

You must use UTF-8 encoding *without BOM* for configuration files.

</div>

<div id="configuration-file-paths" class="section">

## <a href="#toc-entry-186" class="toc-backref">Configuration file paths</a>

Geany has default configuration files installed for the system and also per-user configuration files.

The system files should not normally be edited because they will be overwritten when upgrading Geany.

The user configuration directory can be overridden with the <span class="pre">-c</span> switch, but this is not normally done. See <a href="#command-line-options" class="reference internal">Command line options</a>.

<div class="admonition note">

Note

Any missing subdirectories in the user configuration directory will be created when Geany starts.

</div>

You can check the paths Geany is using with *Help-\>Debug Messages*. Near the top there should be 2 lines with something like:

``` literal-block
Geany-INFO: System data dir: /usr/share/geany
Geany-INFO: User config dir: /home/username/.config/geany
```

<div id="paths-on-unix-like-systems" class="section">

### <a href="#toc-entry-187" class="toc-backref">Paths on Unix-like systems</a>

The system path is $prefix/share/geany, where $prefix is the path where Geany is installed (see <a href="#installation-prefix" class="reference internal">Installation prefix</a>).

The user configuration directory is normally: <span class="pre">/home/username/.config/geany</span>

</div>

<div id="paths-on-windows" class="section">

### <a href="#toc-entry-188" class="toc-backref">Paths on Windows</a>

The system path is the data subfolder of the installation path on Windows.

The user configuration directory might vary, but on Windows XP it's: <span class="pre">C:\\Documents</span> and Settings\\UserName\\Application Data\\geany On Windows 7 and above you most likely will find it at: <span class="pre">C:\\users\\UserName\\Roaming\\geany</span>

</div>

</div>

<div id="tools-menu-items" class="section">

## <a href="#toc-entry-189" class="toc-backref">Tools menu items</a>

There's a *Configuration files* submenu in the *Tools* menu that contains items for some of the available user configuration files. Clicking on one opens it in the editor for you to update. Geany will reload the file after you have saved it.

<div class="admonition note">

Note

Other configuration files not shown here will need to be opened manually, and will not be automatically reloaded when saved. (see *Reload Configuration* below).

</div>

There's also a *Reload Configuration* item which can be used if you updated one of the other configuration files, or modified or added template files.

*Reload Configuration* is also necessary to update syntax highlighting colors.

<div class="admonition note">

Note

Syntax highlighting colors aren't updated in open documents after saving filetypes.common as this may take a significant amount of time.

</div>

<div id="customizing-geany-s-appearance-using-gtk-css" class="section">

### <a href="#toc-entry-190" class="toc-backref">Customizing Geany's appearance using GTK+ CSS</a>

To override GTK+ CSS styles, you can use traditional mechanisms or you can use the *Tools-\>Configuration files* menu to open a file named geany.css which will be loaded after other CSS styles are applied to allow overriding the default styles.

Geany offers a number of CSS IDs which can be used to taylor its appearance. Among the more interesting include:

-   <span class="pre">geany-compiler-context</span> - the style used for build command output surrounding errors
-   <span class="pre">geany-compiler-error</span> - the style used for build command errors
-   <span class="pre">geany-compiler-message</span> - the style other output encountered while running build command
-   <span class="pre">geany-document-status-changed</span> - the style for document tab labels when the document is changed
-   <span class="pre">geany-document-status-disk-changed</span> - the style for document tab labels when the file on disk has changed
-   <span class="pre">geany-document-status-readyonly\`</span> - the style for document tab labels when the document is read-only
-   <span class="pre">geany-search-entry-no-match</span> - the style of find/replace dialog entries when no match is found
-   <span class="pre">geany-terminal-dirty</span> - the style for the message window Terminal tab label when the terminal output has changed.

</div>

</div>

<div id="global-configuration-file" class="section">

## <a href="#toc-entry-191" class="toc-backref">Global configuration file</a>

System administrators can add a global configuration file for Geany which will be used when starting Geany and a user configuration file does not exist.

The global configuration file is read from geany.conf in the system configuration path - see <a href="#configuration-file-paths" class="reference internal">Configuration file paths</a>. It can contain any settings which are found in the usual configuration file created by Geany, but does not have to contain all settings.

<div class="admonition note">

Note

This feature is mainly intended for package maintainers or system admins who want to set up Geany in a multi user environment and set some sane default values for this environment. Usually users won't need to do that.

</div>

</div>

<div id="filetype-definition-files" class="section">

## <a href="#toc-entry-192" class="toc-backref">Filetype definition files</a>

All color definitions and other filetype specific settings are stored in the filetype definition files. Those settings are colors for syntax highlighting, general settings like comment characters or word delimiter characters as well as compiler and linker settings.

See also <a href="#configuration-file-paths" class="reference internal">Configuration file paths</a>.

<div id="filenames" class="section">

### <a href="#toc-entry-193" class="toc-backref">Filenames</a>

Each filetype has a corresponding filetype definition file. The format for built-in filetype Foo is:

``` literal-block
filetypes.foo
```

The extension is normally just the filetype name in lower case.

However there are some exceptions:

| Filetype      | Extension |
|---------------|-----------|
| C++           | cpp       |
| C#            | cs        |
| Make          | makefile  |
| Matlab/Octave | matlab    |

There is also the <a href="#special-file-filetypes-common" class="reference internal">special file filetypes.common</a>.

For <a href="#custom-filetypes" class="reference internal">custom filetypes</a>, the filename for Foo is different:

``` literal-block
filetypes.Foo.conf
```

See the link for details.

</div>

<div id="system-files" class="section">

### <a href="#toc-entry-194" class="toc-backref">System files</a>

The system-wide filetype configuration files can be found in the system configuration path and are called <span class="pre">filetypes.$ext</span>, where $ext is the name of the filetype. For every filetype there is a corresponding definition file. There is one exception: filetypes.common -- this file is for general settings, which are not specific to a certain filetype.

<div class="admonition warning">

Warning

It is not recommended that users edit the system-wide files, because they will be overridden when Geany is updated.

</div>

</div>

<div id="user-files" class="section">

### <a href="#toc-entry-195" class="toc-backref">User files</a>

To change the settings, copy a file from the system configuration path to the subdirectory filedefs in your user configuration directory. Then you can edit the file and the changes will still be available after an update of Geany.

Alternatively, you can create the file yourself and add only the settings you want to change. All missing settings will be read from the corresponding system configuration file.

</div>

<div id="custom-filetypes" class="section">

### <a href="#toc-entry-196" class="toc-backref">Custom filetypes</a>

At startup Geany looks for <span class="pre">filetypes.\*.conf</span> files in the system and user filetype paths, adding any filetypes found with the name matching the '\*' wildcard - e.g. filetypes.Bar.conf.

Custom filetypes are not as powerful as built-in filetypes, but support for the following has been implemented:

-   Recognizing and setting the filetype (after the user has manually updated the <a href="#filetype-extensions" class="reference internal">filetype extensions</a> file).

-   Reading filetype settings in the \[settings\] section, including:  
    -   Using an existing syntax highlighting lexer (<a href="#lexer-filetype" class="reference internal">lexer_filetype</a> key).
    -   Using an existing tags parser (<a href="#tag-parser" class="reference internal">tag_parser</a> key).

-   Build commands (<span class="pre">\[build-menu\]</span> section).

-   Loading global tags files (sharing the tag_parser filetype's namespace).

See <a href="#filetype-configuration" class="reference internal">Filetype configuration</a> for details on each setting.

<div id="creating-a-custom-filetype-from-an-existing-filetype" class="section">

#### <a href="#toc-entry-197" class="toc-backref">Creating a custom filetype from an existing filetype</a>

Because most filetype settings will relate to the syntax highlighting (e.g. styling, keywords, lexer_properties sections), it is best to copy an existing filetype file that uses the lexer you wish to use as the basis of a custom filetype, using the correct filename extension format shown above, e.g.:

``` literal-block
cp filetypes.foo filetypes.Bar.conf
```

Then add the lexer_filetype=Foo setting (if not already present) and add/adjust other settings.

<div class="admonition warning">

Warning

The \[styling\] and \[keywords\] sections have key names specific to each filetype/lexer. You must follow the same names - in particular, some lexers only support one keyword list, or none.

</div>

</div>

</div>

<div id="filetype-configuration" class="section">

### <a href="#toc-entry-198" class="toc-backref">Filetype configuration</a>

As well as the sections listed below, each filetype file can contain a \[build-menu\] section as described in <a href="#build-menu-section" class="reference internal">[build-menu] section</a>.

<div id="styling-section" class="section">

#### <a href="#toc-entry-199" class="toc-backref">[styling] section</a>

In this section the colors for syntax highlighting are defined. The manual format is:

-   key=foreground_color;background_color;bold_flag;italic_flag

Colors have to be specified as RGB hex values prefixed by 0x or \# similar to HTML/CSS hex triplets. For example, all of the following are valid values for pure red; 0xff0000, 0xf00, \#ff0000, or \#f00. The values are case-insensitive but it is a good idea to use lower-case. Note that you can also use *named colors* as well by substituting the color value with the name of a color as defined in the \[named_colors\] section, see the <a href="#named-colors-section" class="reference internal">[named_colors] Section</a> for more information.

Bold and italic are flags and should only be "true" or "false". If their value is something other than "true" or "false", "false" is assumed.

You can omit fields to use the values from the style named "default".

E.g. <span class="pre">key=0xff0000;;true</span>

This makes the key style have red foreground text, default background color text and bold emphasis.

<div id="using-a-named-style" class="section">

##### <a href="#toc-entry-200" class="toc-backref">Using a named style</a>

The second format uses a *named style* name to reference a style defined in filetypes.common.

-   key=named_style
-   key2=named_style2,bold,italic

The bold and italic parts are optional, and if present are used to toggle the bold or italic flags to the opposite of the named style's flags. In contrast to style definition booleans, they are a literal ",bold,italic" and commas are used instead of semi-colons.

E.g. key=comment,italic

This makes the key style match the "comment" named style, but with italic emphasis.

To define named styles, see the filetypes.common <a href="#named-styles-section" class="reference internal">[named_styles] Section</a>.

</div>

<div id="reading-styles-from-another-filetype" class="section">

##### <a href="#toc-entry-201" class="toc-backref">Reading styles from another filetype</a>

You can automatically copy all of the styles from another filetype definition file by using the following syntax for the \[styling\] group:

``` literal-block
[styling=Foo]
```

Where Foo is a filetype name. The corresponding \[styling\] section from filetypes.foo will be read.

This is useful when the same lexer is being used for multiple filetypes (e.g. C/C++/C#/Java/etc). For example, to make the C++ styling the same as the C styling, you would put the following in filetypes.cpp:

``` literal-block
[styling=C]
```

</div>

</div>

<div id="keywords-section" class="section">

#### <a href="#toc-entry-202" class="toc-backref">[keywords] section</a>

This section contains keys for different keyword lists specific to the filetype. Some filetypes do not support keywords, so adding a new key will not work. You can only add or remove keywords to/from an existing list.

<div class="admonition important">

Important

The keywords list must be in one line without line ending characters.

</div>

</div>

<div id="lexer-properties-section" class="section">

#### <a href="#toc-entry-203" class="toc-backref">[lexer_properties] section</a>

Here any special properties for the Scintilla lexer can be set in the format key.name.field=some.value.

Properties Geany uses are listed in the system filetype files. To find other properties you need Geany's source code:

``` literal-block
egrep -o 'GetProperty\w*\("([^"]+)"[^)]+\)' scintilla/Lex*.cxx
```

</div>

<div id="settings-section" class="section">

#### <a href="#toc-entry-204" class="toc-backref">[settings] section</a>

extension  
This is the default file extension used when saving files, not including the period character (.). The extension used should match one of the patterns associated with that filetype (see <a href="#filetype-extensions" class="reference internal">Filetype extensions</a>).

*Example:* extension=cxx

wordchars  
These characters define word boundaries when making selections and searching using word matching options.

*Example:* (look at system filetypes.\* files)

<div class="admonition note last">

Note

This overrides the *wordchars* filetypes.common setting, and has precedence over the *whitespace_chars* setting.

</div>

comment_single  
A character or string which is used to comment code. If you want to use multiline comments only, don't set this but rather comment_open and comment_close.

Single-line comments are used in priority over multiline comments to comment a line, e.g. with the Comment/Uncomment line command.

*Example:* <span class="pre">comment_single=//</span>

comment_open  
A character or string which is used to comment code. You need to also set comment_close to really use multiline comments. If you want to use single-line comments, prefer setting comment_single.

Multiline comments are used in priority over single-line comments to comment a block, e.g. template comments.

*Example:* <span class="pre">comment_open=/\*</span>

comment_close  
If multiline comments are used, this is the character or string to close the comment.

*Example:* <span class="pre">comment_close=\*/</span>

comment_use_indent  
Set this to false if a comment character or string should start at column 0 of a line. If set to true it uses any indentation of the line.

Note: Comment indentation

comment_use_indent=true would generate this if a line is commented (e.g. with Ctrl-D):

``` literal-block
#command_example();
```

comment_use_indent=false would generate this if a line is commented (e.g. with Ctrl-D):

``` literal-block
#   command_example();
```

Note: This setting only works for single line comments (like '//', '#' or ';').

*Example:* comment_use_indent=true

context_action_cmd  
A command which can be executed on the current word or the current selection.

Example usage: Open the API documentation for the current function call at the cursor position.

The command can be set for every filetype or if not set, a global command will be used. The command itself can be specified without the full path, then it is searched in $PATH. But for security reasons, it is recommended to specify the full path to the command. The wildcard %s will be replaced by the current word at the cursor position or by the current selection.

Hint: for PHP files the following could be quite useful: context_action_cmd=firefox "<a href="https://www.php.net/%s" class="reference external">https://www.php.net/%s</a>"

*Example:* context_action_cmd=devhelp <span class="pre">-s</span> "%s"

<!-- -->

tag_parser  
The TagManager language name, e.g. "C". Usually the same as the filetype name.

<!-- -->

lexer_filetype  
A filetype name to setup syntax highlighting from another filetype. This must not be recursive, i.e. it should be a filetype name that doesn't use the *lexer_filetype* key itself, e.g.:

``` literal-block
lexer_filetype=C
#lexer_filetype=C++
```

The second line is wrong, because filetypes.cpp itself uses lexer_filetype=C, which would be recursive.

symbol_list_sort_mode  
What the default symbol list sort order should be.

| Value | Meaning                                  |
|-------|------------------------------------------|
| 0     | Sort symbols by name                     |
| 1     | Sort symbols by appearance (line number) |

<!-- -->

xml_indent_tags  
If this setting is set to *true*, a new line after a line ending with an unclosed XML/HTML tag will be automatically indented. This only applies to filetypes for which the HTML or XML lexer is used. Such filetypes have this setting in their system configuration files.

mime_type  
The MIME type for this file type, e.g. "text/x-csrc". This is used for example to chose the icon to display for this file type.

</div>

<div id="indentation-section" class="section">

#### <a href="#toc-entry-205" class="toc-backref">[indentation] section</a>

This section allows definition of default indentation settings specific to the file type, overriding the ones configured in the preferences. This can be useful for file types requiring specific indentation settings (e.g. tabs only for Makefile). These settings don't override auto-detection if activated.

width  
The forced indentation width.

type  
The forced indentation type.

| Value | Indentation type        |
|-------|-------------------------|
| 0     | Spaces only             |
| 1     | Tabs only               |
| 2     | Mixed (tabs and spaces) |

</div>

<div id="build-menu-filetype-section" class="section">

#### <a href="#toc-entry-206" class="toc-backref">[build-menu] filetype section</a>

This supports the same keys as the geany.conf <a href="#build-menu-section" class="reference internal">[build-menu] section</a>.

Example:

``` literal-block
FT_00_LB=_Compile
FT_00_CM=gcc -c "%f"
FT_00_WD=
FT_01_LB=_Build
FT_01_CM=gcc -o "%e" "%f"
FT_01_WD=
EX_00_LB=_Execute
EX_00_CM="./%e"
EX_00_WD=
error_regex=^([^:]+):([0-9]+):
```

</div>

<div id="build-settings-section" class="section">

#### <a href="#toc-entry-207" class="toc-backref">[build_settings] section</a>

As of Geany 0.19 this section is for legacy support. Values that are set in the \[build-menu\] section will override those in this section.

If any build menu item settings have been configured in the <a href="#set-build-commands-dialog" class="reference internal">Set Build Commands dialog</a> (or the *Build* tab of the <a href="#project-properties" class="reference internal">Project Properties</a> dialog), then these settings are stored in the \[build-menu\] section and will override the settings in this section for that item.

error_regex  
See the \[build-menu\] section for details.

**Build commands**

compiler  
This item specifies the command to compile source code files. But it is also possible to use it with interpreted languages like Perl or Python. With these filetypes you can use this option as a kind of syntax parser, which sends output to the compiler message window.

You should quote the filename to also support filenames with spaces. The following wildcards for filenames are available:

-   %f -- complete filename without path
-   %e -- filename without path and without extension

*Example:* compiler=gcc <span class="pre">-Wall</span> <span class="pre">-c</span> "%f"

linker  
This item specifies the command to link the file. If the file is not already compiled, it will be compiled while linking. The -o option is automatically added by Geany. This item works well with GNU gcc, but may be problematic with other compilers (esp. with the linker).

*Example:* linker=gcc <span class="pre">-Wall</span> "%f"

run_cmd  
Use this item to execute your file. It has to have been built already. Use the %e wildcard to have only the name of the executable (i.e. without extension) or use the %f wildcard if you need the complete filename, e.g. for shell scripts.

*Example:* <span class="pre">run_cmd="./%e"</span>

</div>

</div>

<div id="special-file-filetypes-common" class="section">

### <a href="#toc-entry-208" class="toc-backref">Special file filetypes.common</a>

There is a special filetype definition file called filetypes.common. This file defines some general non-filetype-specific settings.

You can open the user filetypes.common with the *Tools-\>Configuration Files-\>filetypes.common* menu item. This adds the default settings to the user file if the file doesn't exist. Alternatively the file can be created manually, adding only the settings you want to change. All missing settings will be read from the system file.

<div class="admonition note">

Note

See the <a href="#filetype-configuration" class="reference internal">Filetype configuration</a> section for how to define styles.

</div>

<div id="named-styles-section" class="section">

#### <a href="#toc-entry-209" class="toc-backref">[named_styles] section</a>

Named styles declared here can be used in the \[styling\] section of any filetypes.\* file.

For example:

*In filetypes.common*:

``` literal-block
[named_styles]
foo=0xc00000;0xffffff;false;true
bar=foo
```

*In filetypes.c*:

``` literal-block
[styling]
comment=foo
```

This saves copying and pasting the whole style definition into several different files.

<div class="admonition note">

Note

You can define aliases for named styles, as shown with the bar entry in the above example, but they must be declared after the original style.

</div>

</div>

<div id="named-colors-section" class="section">

#### <a href="#toc-entry-210" class="toc-backref">[named_colors] section</a>

Named colors declared here can be used in the \[styling\] or \[named_styles\] section of any filetypes.\* file or color scheme.

For example:

``` literal-block
[named_colors]
my_red_color=#FF0000
my_blue_color=#0000FF

[named_styles]
foo=my_red_color;my_blue_color;false;true
```

This allows to define a color palette by name so that to change a color scheme-wide only involves changing the hex value in a single location.

</div>

<div id="styling-section-1" class="section">

#### <a href="#toc-entry-211" class="toc-backref">[styling] section</a>

default  
This is the default style. It is used for styling files without a filetype set.

*Example:* default=0x000000;0xffffff;false;false

selection  
The style for coloring selected text. The format is:

-   Foreground color
-   Background color
-   Use foreground color
-   Use background color

The colors are only set if the 3rd or 4th argument is true. When the colors are not overridden, the default is a dark grey background with syntax highlighted foreground text.

*Example:* selection=0xc0c0c0;0x00007F;true;true

brace_good  
The style for brace highlighting when a matching brace was found.

*Example:* brace_good=0xff0000;0xFFFFFF;true;false

brace_bad  
The style for brace highlighting when no matching brace was found.

*Example:* brace_bad=0x0000ff;0xFFFFFF;true;false

caret  
The style for coloring the caret(the blinking cursor). Only first and third argument is interpreted. Set the third argument to true to change the caret into a block caret.

*Example:* caret=0x000000;0x0;false;false

caret_width  
The width for the caret(the blinking cursor). Only the first argument is interpreted. The width is specified in pixels with a maximum of three pixel. Use the width 0 to make the caret invisible.

*Example:* caret_width=3

current_line  
The style for coloring the background of the current line. Only the second and third arguments are interpreted. The second argument is the background color. Use the third argument to enable or disable background highlighting for the current line (has to be true/false).

*Example:* current_line=0x0;0xe5e5e5;true;false

indent_guide  
The style for coloring the indentation guides. Only the first and second arguments are interpreted.

*Example:* indent_guide=0xc0c0c0;0xffffff;false;false

white_space  
The style for coloring the white space if it is shown. The first both arguments define the foreground and background colors, the third argument sets whether to use the defined foreground color or to use the color defined by each filetype for the white space. The fourth argument defines whether to use the background color.

*Example:* white_space=0xc0c0c0;0xffffff;true;true

margin_linenumber  
Line number margin foreground and background colors.

<!-- -->

margin_folding  
Fold margin foreground and background colors.

fold_symbol_highlight  
Highlight color of folding symbols.

folding_style  
The style of folding icons. Only first and second arguments are used.

Valid values for the first argument are:

-   1 -- for boxes
-   2 -- for circles
-   3 -- for arrows
-   4 -- for +/-

Valid values for the second argument are:

-   0 -- for no lines
-   1 -- for straight lines
-   2 -- for curved lines

*Default:* folding_style=1;1;

*Arrows:* folding_style=3;0;

folding_horiz_line  
Draw a thin horizontal line at the line where text is folded. Only first argument is used.

Valid values for the first argument are:

-   0 -- disable, do not draw a line
-   1 -- draw the line above folded text
-   2 -- draw the line below folded text

*Example:* folding_horiz_line=0;0;false;false

line_wrap_visuals  
First argument: drawing of visual flags to indicate a line is wrapped. This is a bitmask of the values:

-   0 -- No visual flags
-   1 -- Visual flag at end of subline of a wrapped line
-   2 -- Visual flag at begin of subline of a wrapped line. Subline is indented by at least 1 to make room for the flag.

Second argument: whether the visual flags to indicate a line is wrapped are drawn near the border or near the text. This is a bitmask of the values:

-   0 -- Visual flags drawn near border
-   1 -- Visual flag at end of subline drawn near text
-   2 -- Visual flag at begin of subline drawn near text

Only first and second arguments are interpreted.

*Example:* line_wrap_visuals=3;0;false;false

line_wrap_indent  
First argument: sets the size of indentation of sublines for wrapped lines in terms of the width of a space, only used when the second argument is 0.

Second argument: wrapped sublines can be indented to the position of their first subline or one more indent level. Possible values:

-   0 - Wrapped sublines aligned to left of window plus amount set by the first argument
-   1 - Wrapped sublines are aligned to first subline indent (use the same indentation)
-   2 - Wrapped sublines are aligned to first subline indent plus one more level of indentation

Only first and second arguments are interpreted.

*Example:* line_wrap_indent=0;1;false;false

translucency  
Translucency for the current line (first argument) and the selection (second argument). Values between 0 and 256 are accepted.

Note for Windows 95, 98 and ME users: keep this value at 256 to disable translucency otherwise Geany might crash.

Only the first and second arguments are interpreted.

*Example:* translucency=256;256;false;false

marker_line  
The style for a highlighted line (e.g when using *Go to line* or *Go to symbol*). The foreground color (first argument) is only used when the Markers margin is enabled (see View menu).

Only the first and second arguments are interpreted.

*Example:* marker_line=0x000000;0xffff00;false;false

marker_search  
The style for a marked search results (when using "Mark" in Search dialogs). The second argument sets the background color for the drawn rectangle.

Only the second argument is interpreted.

*Example:* marker_search=0x000000;0xb8f4b8;false;false

marker_mark  
The style for a marked line (e.g when using the "Toggle Marker" keybinding (Ctrl-M)). The foreground color (first argument) is only used when the Markers margin is enabled (see View menu).

Only the first and second arguments are interpreted.

*Example:* marker_mark=0x000000;0xb8f4b8;false;false

marker_translucency  
Translucency for the line marker (first argument) and the search marker (second argument). Values between 0 and 256 are accepted.

Note for Windows 95, 98 and ME users: keep this value at 256 to disable translucency otherwise Geany might crash.

Only the first and second arguments are interpreted.

*Example:* marker_translucency=256;256;false;false

line_height  
Amount of space to be drawn above and below the line's baseline. The first argument defines the amount of space to be drawn above the line, the second argument defines the amount of space to be drawn below.

Only the first and second arguments are interpreted.

*Example:* line_height=0;0;false;false

calltips  
The style for coloring the calltips. The first two arguments define the foreground and background colors, the third and fourth arguments set whether to use the defined colors.

*Example:* calltips=0xc0c0c0;0xffffff;false;false

indicator_error  
The color of the error indicator.

Only the first argument (foreground color) is used.

*Example:* indicator_error=0xff0000

</div>

<div id="settings-section-1" class="section">

#### <a href="#toc-entry-212" class="toc-backref">[settings] section</a>

whitespace_chars  
Characters to treat as whitespace. These characters are ignored when moving, selecting and deleting across word boundaries (see <a href="#scintilla-keyboard-commands" class="reference internal">Scintilla keyboard commands</a>).

This should include space (\\s) and tab (\\t).

*Example:* <span class="pre">whitespace_chars=\\s\\t!\\"#$%&'()\*+,-./:;\<=\>?@\[\\\\\]^\`{\|}\~</span>

wordchars  
These characters define word boundaries when making selections and searching using word matching options.

*Example:* wordchars=\_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

<div class="admonition note last">

Note

This has precedence over the *whitespace_chars* setting.

</div>

</div>

</div>

</div>

<div id="filetype-extensions" class="section">

## <a href="#toc-entry-213" class="toc-backref">Filetype extensions</a>

<div class="admonition note">

Note

To change the default filetype extension used when saving a new file, see <a href="#filetype-definition-files" class="reference internal">Filetype definition files</a>.

</div>

You can override the list of file extensions that Geany uses to detect filetypes using the user filetype_extensions.conf file. Use the *Tools-\>Configuration Files-\>filetype_extensions.conf* menu item. See also <a href="#configuration-file-paths" class="reference internal">Configuration file paths</a>.

You should only list lines for filetype extensions that you want to override in the user configuration file and remove or comment out others. The patterns are listed after the = sign, using a semi-colon separated list of patterns which should be matched for that filetype.

For example, to override the filetype extensions for Make, the file should look like:

``` literal-block
[Extensions]
Make=Makefile*;*.mk;Buildfile;
```

</div>

<div id="preferences-file-format" class="section">

## <a href="#toc-entry-214" class="toc-backref">Preferences file format</a>

The user preferences file geany.conf holds settings for all the items configured in the preferences dialog. This file should not be edited while Geany is running as the file will be overwritten when the preferences in Geany are changed or Geany is quit.

<div id="build-menu-section" class="section">

### <a href="#toc-entry-215" class="toc-backref">[build-menu] section</a>

The \[build-menu\] section contains the configuration of the build menu. This section can occur in filetype, preferences and project files and always has the format described here. Different menu items are loaded from different files, see the table in the <a href="#build-menu-configuration" class="reference internal">Build Menu Configuration</a> section for details. All the settings can be configured from the dialogs except the execute command in filetype files and filetype definitions in the project file, so these are the only ones which need hand editing.

<div id="menu-commands" class="section">

#### <a href="#toc-entry-216" class="toc-backref">Menu commands</a>

The build-menu section stores one entry for each setting for each menu item that is configured. The keys for these settings have the format:

> GG_NN_FF

where:

-   GG - is the menu item group,
    -   FT for filetype build
    -   NF for independent (non-filetype) build
    -   EX for execute
-   NN - is a two decimal digit number of the item within the group, starting at 00
-   FF - is the field,
    -   LB for label
    -   CM for command
    -   WD for working directory

See <a href="#build-menu-filetype-section" class="reference internal">[build-menu] filetype section</a> for an example.

</div>

<div id="error-regular-expression" class="section">

#### <a href="#toc-entry-217" class="toc-backref">Error regular expression</a>

error_regex  
This is a Perl-compatible regular expression (PCRE) to parse a filename (absolute or relative) and line number from the build output. If undefined, Geany will fall back to its default error message parsing.

Only the first two match groups will be read by Geany. These groups can occur in any order: the match group consisting of only digits will be used as the line number, and the other group as the filename. In no group consists of only digits, the match will fail.

*Example:* <span class="pre">error_regex=^(.+):(\[0-9\]+):\[0-9\]+</span>

This will parse a message such as: test.py:7:24: E202 whitespace before '\]'

</div>

</div>

</div>

<div id="project-file-format" class="section">

## <a href="#toc-entry-218" class="toc-backref">Project file format</a>

The project file contains project related settings and possibly a record of the current session files.

<div id="build-menu-additions" class="section">

### <a href="#toc-entry-219" class="toc-backref">[build-menu] additions</a>

The project file also can have extra fields in the \[build-menu\] section in addition to those listed in <a href="#build-menu-section" class="reference internal">[build-menu] section</a> above.

When filetype menu items are configured for the project they are stored in the project file.

The filetypes entry is a list of the filetypes which exist in the project file.

For each filetype the entries for that filetype have the format defined in <a href="#build-menu-section" class="reference internal">[build-menu] section</a> but the key is prefixed by the name of the filetype as it appears in the filetypes entry, eg the entry for the label of filetype menu item 0 for the C filetype would be

> CFT_00_LB=Label

</div>

</div>

<div id="templates" class="section">

## <a href="#toc-entry-220" class="toc-backref">Templates</a>

Geany supports the following templates:

-   ChangeLog entry
-   File header
-   Function description
-   Short GPL notice
-   Short BSD notice
-   File templates

To use these templates, just open the Edit menu or open the popup menu by right-clicking in the editor widget, and choose "Insert Comments" and insert templates as you want.

Some templates (like File header or ChangeLog entry) will always be inserted at the top of the file.

To insert a function description, the cursor must be inside of the function, so that the function name can be determined automatically. The description will be positioned correctly one line above the function, just check it out. If the cursor is not inside of a function or the function name cannot be determined, the inserted function description won't contain the correct function name but "unknown" instead.

<div class="admonition note">

Note

Geany automatically reloads template information when it notices you save a file in the user's template configuration directory. You can also force this by selecting *Tools-\>Reload Configuration*.

</div>

<div id="template-meta-data" class="section">

### <a href="#toc-entry-221" class="toc-backref">Template meta data</a>

Meta data can be used with all templates, but by default user set meta data is only used for the ChangeLog and File header templates.

In the configuration dialog you can find a tab "Templates" (see <a href="#template-preferences" class="reference internal">Template preferences</a>). You can define the default values which will be inserted in the templates.

</div>

<div id="file-templates" class="section">

### <a href="#toc-entry-222" class="toc-backref">File templates</a>

File templates are templates used as the basis of a new file. To use them, choose the *New (with Template)* menu item from the *File* menu. If there is more than one template for a filetype then they will be grouped in a submenu.

By default, file templates are installed for some filetypes. Custom file templates can be added by creating the appropriate template file. You can also edit the default file templates.

The file's contents are just the text to place in the document, with optional template wildcards like {fileheader}. The fileheader wildcard can be placed anywhere, but it's usually put on the first line of the file, followed by a blank line.

<div id="adding-file-templates" class="section">

#### <a href="#toc-entry-223" class="toc-backref">Adding file templates</a>

File templates are read from templates/files under the <a href="#configuration-file-paths" class="reference internal">Configuration file paths</a>.

The filetype to use is detected from the template file's extension, if any. For example, creating a file module.c would add a menu item which created a new document with the filetype set to 'C'.

The template file is read from disk when the corresponding menu item is clicked.

</div>

</div>

<div id="customizing-templates" class="section">

### <a href="#toc-entry-224" class="toc-backref">Customizing templates</a>

Each template can be customized to your needs. The templates are stored in the <span class="pre">\~/.config/geany/templates/</span> directory (see the section called <a href="#command-line-options" class="reference internal">Command line options</a> for further information about the configuration directory). Just open the desired template with an editor (ideally, Geany ;-) ) and edit the template to your needs. There are some wildcards which will be automatically replaced by Geany at startup.

<div id="template-wildcards" class="section">

#### <a href="#toc-entry-225" class="toc-backref">Template wildcards</a>

All wildcards must be enclosed by "{" and "}", e.g. {date}.

**Wildcards for character escaping**

| Wildcard | Description                                                       | Available in                           |
|----------|-------------------------------------------------------------------|----------------------------------------|
| ob       | { Opening Brace (used to prevent other wildcards being expanded). | file templates, file header, snippets. |
| cb       | } Closing Brace.                                                  | file templates, file header, snippets. |
| pc       | % Percent (used to escape e.g. %block% in snippets).              | snippets.                              |

<div id="global-wildcards" class="section">

##### <a href="#toc-entry-226" class="toc-backref">Global wildcards</a>

These are configurable, see <a href="#template-preferences" class="reference internal">Template preferences</a>.

| Wildcard  | Description                                                                         | Available in                                                                            |
|-----------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| developer | The name of the developer.                                                          | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |
| initial   | The developer's initials, e.g. "ET" for Enrico Tröger or "JFD" for John Foobar Doe. | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |
| mail      | The email address of the developer.                                                 | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |
| company   | The company the developer is working for.                                           | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |
| version   | The initial version of a new file.                                                  | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |

</div>

<div id="date-time-wildcards" class="section">

##### <a href="#toc-entry-227" class="toc-backref">Date &amp; time wildcards</a>

The format for these wildcards can be changed in the preferences dialog, see <a href="#template-preferences" class="reference internal">Template preferences</a>. For a list of available conversion specifiers see <a href="https://docs.gtk.org/glib/method.DateTime.format.html" class="reference external">https://docs.gtk.org/glib/method.DateTime.format.html</a>.

| Wildcard | Description                                                          | Available in                                                                            |
|----------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| year     | The current year. Default format is: YYYY.                           | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |
| date     | The current date. Default format: YYYY-MM-DD.                        | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |
| datetime | The current date and time. Default format: DD.MM.YYYY HH:mm:ss ZZZZ. | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |

</div>

<div id="dynamic-wildcards" class="section">

##### <a href="#toc-entry-228" class="toc-backref">Dynamic wildcards</a>

| Wildcard     | Description                                                                                                                                                                                                 | Available in                                                                            |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| untitled     | The string "untitled" (this will be translated to your locale), used in file templates.                                                                                                                     | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |
| geanyversion | The actual Geany version, e.g. "Geany 2.1".                                                                                                                                                                 | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |
| filename     | The filename of the current file. For new files, it's only replaced when first saving if found on the first 4 lines of the file.                                                                            | file header, snippets, file templates.                                                  |
| project      | The current project's name, if any.                                                                                                                                                                         | file header, snippets, file templates.                                                  |
| description  | The current project's description, if any.                                                                                                                                                                  | file header, snippets, file templates.                                                  |
| functionname | The function name of the function at the cursor position. This wildcard will only be replaced in the function description template.                                                                         | function description.                                                                   |
| command:path | Executes the specified command and replace the wildcard with the command's standard output. See <a href="#special-command-wildcard" class="reference internal">Special {command:} wildcard</a> for details. | file templates, file header, function description, ChangeLog entry, bsd, gpl, snippets. |

</div>

<div id="template-insertion-wildcards" class="section">

##### <a href="#toc-entry-229" class="toc-backref">Template insertion wildcards</a>

| Wildcard   | Description                                                                      | Available in              |
|------------|----------------------------------------------------------------------------------|---------------------------|
| gpl        | This wildcard inserts a short GPL notice.                                        | file header.              |
| bsd        | This wildcard inserts a BSD licence notice.                                      | file header.              |
| fileheader | The file header template. This wildcard will only be replaced in file templates. | snippets, file templates. |

</div>

<div id="special-command-wildcard" class="section">

##### <a href="#toc-entry-230" class="toc-backref">Special {command:} wildcard</a>

The {command:} wildcard is a special one because it can execute a specified command and put the command's output (stdout) into the template.

Example:

``` literal-block
{command:uname -a}
```

will result in:

``` literal-block
Linux localhost 2.6.9-023stab046.2-smp #1 SMP Mon Dec 10 15:04:55 MSK 2007 x86_64 GNU/Linux
```

Using this wildcard you can insert nearly any arbitrary text into the template.

In the environment of the executed command the variables GEANY_FILENAME, GEANY_FILETYPE and GEANY_FUNCNAME are set. The value of these variables is filled in only if Geany knows about it. For example, GEANY_FUNCNAME is only filled within the function description template. However, these variables are *always* set, just maybe with an empty value. You can easily access them e.g. within an executed shell script using:

``` literal-block
$GEANY_FILENAME
```

<div class="admonition note">

Note

If the specified command could not be found or not executed, the wildcard is substituted by an empty string. In such cases, you can find the occurred error message on Geany's standard error and in the *Help-\>Debug Messages* dialog.

</div>

</div>

</div>

</div>

</div>

<div id="customizing-the-toolbar" class="section">

## <a href="#toc-entry-231" class="toc-backref">Customizing the toolbar</a>

You can add, remove and reorder the elements in the toolbar by using the toolbar editor, or by manually editing the configuration file ui_toolbar.xml.

The toolbar editor can be opened from the preferences editor on the Toolbar tab or by right-clicking on the toolbar itself and choosing it from the menu.

<div id="manually-editing-the-toolbar-layout" class="section">

### <a href="#toc-entry-232" class="toc-backref">Manually editing the toolbar layout</a>

To override the system-wide configuration file, copy it to your user configuration directory (see <a href="#configuration-file-paths" class="reference internal">Configuration file paths</a>).

For example:

``` literal-block
% cp /usr/local/share/geany/ui_toolbar.xml /home/username/.config/geany/
```

Then edit it and add any of the available elements listed in the file or remove any of the existing elements. Of course, you can also reorder the elements as you wish and add or remove additional separators. This file must be valid XML, otherwise the global toolbar UI definition will be used instead.

Your changes are applied once you save the file.

<div class="admonition note">

Note

1.  You cannot add new actions which are not listed below.
2.  Everything you add or change must be inside the /ui/toolbar/ path.

</div>

</div>

<div id="available-toolbar-elements" class="section">

### <a href="#toc-entry-233" class="toc-backref">Available toolbar elements</a>

| Element name | Description                                                                                                                                                                              |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| New          | Create a new file                                                                                                                                                                        |
| Open         | Open an existing file                                                                                                                                                                    |
| Save         | Save the current file                                                                                                                                                                    |
| SaveAll      | Save all open files                                                                                                                                                                      |
| Reload       | Reload the current file from disk                                                                                                                                                        |
| Close        | Close the current file                                                                                                                                                                   |
| CloseAll     | Close all open files                                                                                                                                                                     |
| Print        | Print the current file                                                                                                                                                                   |
| Cut          | Cut the current selection                                                                                                                                                                |
| Copy         | Copy the current selection                                                                                                                                                               |
| Paste        | Paste the contents of the clipboard                                                                                                                                                      |
| Delete       | Delete the current selection                                                                                                                                                             |
| Undo         | Undo the last modification                                                                                                                                                               |
| Redo         | Redo the last modification                                                                                                                                                               |
| NavBack      | Navigate back a location                                                                                                                                                                 |
| NavFor       | Navigate forward a location                                                                                                                                                              |
| Compile      | Compile the current file                                                                                                                                                                 |
| Build        | Build the current file, includes a submenu for Make commands. Geany remembers the last chosen action from the submenu and uses this as default action when the button itself is clicked. |
| Run          | Run or view the current file                                                                                                                                                             |
| Color        | Open a color chooser dialog, to interactively pick colors from a palette                                                                                                                 |
| ZoomIn       | Zoom in the text                                                                                                                                                                         |
| ZoomOut      | Zoom out the text                                                                                                                                                                        |
| UnIndent     | Decrease indentation                                                                                                                                                                     |
| Indent       | Increase indentation                                                                                                                                                                     |
| Replace      | Replace text in the current document                                                                                                                                                     |
| SearchEntry  | The search field belonging to the 'Search' element (can be used alone)                                                                                                                   |
| Search       | Find the entered text in the current file (only useful if you also use 'SearchEntry')                                                                                                    |
| GotoEntry    | The goto field belonging to the 'Goto' element (can be used alone)                                                                                                                       |
| Goto         | Jump to the entered line number (only useful if you also use 'GotoEntry')                                                                                                                |
| Preferences  | Show the preferences dialog                                                                                                                                                              |
| Quit         | Quit Geany                                                                                                                                                                               |

</div>

</div>

</div>

<div id="plugin-documentation" class="section">

# <a href="#toc-entry-234" class="toc-backref">Plugin documentation</a>

<div id="html-characters" class="section">

## <a href="#toc-entry-235" class="toc-backref">HTML Characters</a>

The HTML Characters plugin helps when working with special characters in XML/HTML, e.g. German Umlauts ü and ä.

<div id="insert-entity-dialog" class="section">

### <a href="#toc-entry-236" class="toc-backref">Insert entity dialog</a>

When the plugin is enabled, you can insert special character entities using *Tools-\>Insert Special HTML Characters*.

This opens up a dialog where you can find a huge amount of special characters sorted by category that you might like to use inside your document. You can expand and collapse the categories by clicking on the little arrow on the left hand side. Once you have found the desired character click on it and choose "Insert". This will insert the entity for the character at the current cursor position. You might also like to double click the chosen entity instead.

</div>

<div id="replace-special-chars-by-its-entity" class="section">

### <a href="#toc-entry-237" class="toc-backref">Replace special chars by its entity</a>

To help make a XML/HTML document valid the plugin supports replacement of special chars known by the plugin. Both bulk replacement and immediate replacement during typing are supported.

A few characters will not be replaced. These are  
-   "
-   &
-   \<
-   \>
-   (&nbsp;)

<div id="at-typing-time" class="section">

#### <a href="#toc-entry-238" class="toc-backref">At typing time</a>

You can activate/deactivate this feature using the *Tools-\>HTML Replacement-\>Auto-replace Special Characters* menu item. If it's activated, all special characters (beside the given exceptions from above) known by the plugin will be replaced by their entities.

You could also set a keybinding for the plugin to toggle the status of this feature.

</div>

<div id="bulk-replacement" class="section">

#### <a href="#toc-entry-239" class="toc-backref">Bulk replacement</a>

After inserting a huge amount of text, e.g. by using copy & paste, the plugin allows bulk replacement of all known characters (beside the mentioned exceptions). You can find the function under the same menu at *Tools-\>HTML Replacement-\>Replace Characters in Selection*, or configure a keybinding for the plugin.

</div>

</div>

</div>

<div id="save-actions" class="section">

## <a href="#toc-entry-240" class="toc-backref">Save Actions</a>

<div id="auto-save" class="section">

### <a href="#toc-entry-241" class="toc-backref">Auto Save</a>

This plugin provides an option to automatically save documents. You can choose to save the current document, or all of your documents, at a given delay.

<div id="save-on-focus-out" class="section">

#### <a href="#toc-entry-242" class="toc-backref">Save on focus out</a>

You can save the current document when the editor's focus goes out. Every pop-up, menu dialogs, or anything else that can make the editor lose the focus, will make the current document to be saved.

</div>

</div>

<div id="backup-copy" class="section">

### <a href="#toc-entry-243" class="toc-backref">Backup Copy</a>

This plugin creates a backup copy of the current file in Geany when it is saved. You can specify the directory where the backup copy is saved and you can configure the automatically added extension in the configure dialog in Geany's plugin manager.

After the plugin was loaded in Geany's plugin manager, every file is copied into the configured backup directory *after* the file has been saved in Geany.

The created backup copy file permissions are set to read-write only for the user. This should help to not create world-readable files on possibly insecure destination directories like /tmp (especially useful on multi-user systems). This applies only to non-Windows systems. On Windows, no explicit file permissions are set.

Additionally, you can define how many levels of the original file's directory structure should be replicated in the backup copy path. For example, setting the option *Directory levels to include in the backup destination* to *2* cause the plugin to create the last two components of the original file's path in the backup copy path and place the new file there.

</div>

<div id="untitled-document-save" class="section">

### <a href="#toc-entry-244" class="toc-backref">Untitled Document Save</a>

This configuration allows to automatically create an underlying file for newly-opened editor tabs (or when using *File-\>New* or *File-\>New (with template)*). File type is set appropriately to the used template. When no template is used - filetype will be determined by the configurable default value. Such functionality is useful when user often creates new files just for quick editing, taking notes, testing code etc.

<div id="instant-save" class="section">

#### <a href="#toc-entry-245" class="toc-backref">Instant Save</a>

In this mode, for each new editor tab opened by the user, the plugin creates a new file with randomly generated name inside the configured directory. This enables users to quickly compile, build and/or run the new file without the need to assign an explicit filename through the Save As dialog.

By default, the operating system temporary directory is used so files are cleaned up after reboot.

</div>

<div id="persistent-untitled-documents" class="section">

#### <a href="#toc-entry-246" class="toc-backref">Persistent Untitled Documents</a>

Unlike Instant Save, which treats untitled documents as temporary files that are automatically deleted, untitled documents in this mode behave more like ordinary files that are stored permanently. Users do not have to worry about saving or restoring such files by themselves - all untitled documents are auto-saved at regular intervals and restored on Geany start or when opening/closing projects.

By default, files backing untitled documents in this mode are stored under the Geany configuration directory.

</div>

</div>

</div>

</div>

<div id="contributing-to-this-document" class="section">

# <a href="#toc-entry-247" class="toc-backref">Contributing to this document</a>

This document (geany.txt) is written in <a href="https://docutils.sourceforge.net/rst.html" class="reference external">reStructuredText</a> (or "reST"). The source file for it is located in Geany's doc subdirectory. If you intend on making changes, you should grab the source right from Git to make sure you've got the newest version. First, you need to configure the build system to generate the HTML documentation passing the *--enable-html-docs* option to the *configure* script. Then after editing the file, run make (from the root build directory or from the *doc* subdirectory) to build the HTML documentation and see how your changes look. This regenerates the geany.html file inside the *doc* subdirectory. To generate a PDF file, configure with *--enable-pdf-docs* and run make as for the HTML version. The generated PDF file is named geany-2.1.pdf and is located inside the *doc* subdirectory.

After you are happy with your changes, create a patch e.g. by using:

``` literal-block
% git diff geany.txt > foo.patch
```

or even better, by creating a Git-formatted patch which will keep authoring and description data, by first committing your changes (doing so in a fresh new branch is recommended for master not to diverge from upstream) and then using git format-patch:

``` literal-block
% git checkout -b my-documentation-changes # create a fresh branch
% git commit geany.txt
Write a good commit message...
% git format-patch HEAD^
% git checkout master # go back to master
```

and then submit that file to the mailing list for review.

Also you can clone the Geany repository at GitHub and send a pull request.

Note, you will need the Python docutils software package installed to build the docs. The package is named <span class="pre">python-docutils</span> on Debian and Fedora systems.

</div>

<div id="scintilla-keyboard-commands" class="section">

# <a href="#toc-entry-248" class="toc-backref">Scintilla keyboard commands</a>

Copyright © 1998, 2006 Neil Hodgson \<neilh(at)scintilla(dot)org\>

This appendix is distributed under the terms of the License for Scintilla and SciTE. A copy of this license can be found in the file scintilla/License.txt included with the source code of this program and in the appendix of this document. See <a href="#license-for-scintilla-and-scite" class="reference internal">License for Scintilla and SciTE</a>.

20 June 2006

<div id="keyboard-commands" class="section">

## <a href="#toc-entry-249" class="toc-backref">Keyboard commands</a>

Keyboard commands for Scintilla mostly follow common Windows and GTK+ conventions. All move keys (arrows, page up/down, home and end) allows to extend or reduce the stream selection when holding the Shift key, and the rectangular selection when holding the appropriate keys (see <a href="#column-mode-editing-rectangular-selections" class="reference internal">Column mode editing (rectangular selections)</a>).

Some keys may not be available with some national keyboards or because they are taken by the system such as by a window manager or GTK. Keyboard equivalents of menu commands are listed in the menus. Some less common commands with no menu equivalent are:

| Action                                       | Shortcut key         |
|----------------------------------------------|----------------------|
| Magnify text size.                           | Ctrl-Keypad+         |
| Reduce text size.                            | Ctrl-Keypad-         |
| Restore text size to normal.                 | Ctrl-Keypad/         |
| Indent block.                                | Tab                  |
| Dedent block.                                | Shift-Tab            |
| Delete to start of word.                     | Ctrl-BackSpace       |
| Delete to end of word.                       | Ctrl-Delete          |
| Delete to start of line.                     | Ctrl-Shift-BackSpace |
| Go to start of document.                     | Ctrl-Home            |
| Extend selection to start of document.       | Ctrl-Shift-Home      |
| Go to start of display line.                 | Alt-Home             |
| Extend selection to start of display line.   | Alt-Shift-Home       |
| Go to end of document.                       | Ctrl-End             |
| Extend selection to end of document.         | Ctrl-Shift-End       |
| Extend selection to end of display line.     | Alt-Shift-End        |
| Previous paragraph. Shift extends selection. | Ctrl-Up              |
| Next paragraph. Shift extends selection.     | Ctrl-Down            |
| Previous word. Shift extends selection.      | Ctrl-Left            |
| Next word. Shift extends selection.          | Ctrl-Right           |

</div>

</div>

<div id="tips-and-tricks" class="section">

# <a href="#toc-entry-250" class="toc-backref">Tips and tricks</a>

<div id="document-notebook" class="section">

## <a href="#toc-entry-251" class="toc-backref">Document notebook</a>

-   Double-click on empty space in the notebook tab bar to open a new document.
-   Middle-click on a document's notebook tab to close the document.
-   Hold Ctrl and click on any notebook tab to switch to the last used document.
-   Double-click on a document's notebook tab to toggle all additional widgets (to show them again use the View menu or the keyboard shortcut). The interface pref must be enabled for this to work.

</div>

<div id="editor" class="section">

## <a href="#toc-entry-252" class="toc-backref">Editor</a>

-   Alt-scroll wheel moves up/down a page.
-   Ctrl-scroll wheel zooms in/out.
-   Shift-scroll wheel scrolls 8 characters right/left.
-   Ctrl-click on a word in a document to perform *Go to Symbol Definition*.
-   Ctrl-click on a bracket/brace to perform *Go to Matching Brace*.

</div>

<div id="sidebar-1" class="section">

## <a href="#toc-entry-253" class="toc-backref">Sidebar</a>

-   Document list  
    -   Middle-click to close a document or all documents in a folder.
    -   When the tree has keyboard focus, typing will match the start of a filename. Press up or down to cycle through matches.

</div>

<div id="gtk-related" class="section">

## <a href="#toc-entry-254" class="toc-backref">GTK-related</a>

-   Notebook tabs - Scrolling the mouse wheel over the tab bar will switch notebook pages. (This was GTK2 default behaviour and still works for the document notebook).
-   Tree views - Double-click on a parent item's text to expand or collapse its children.

The following are derived from X-Windows features (but GTK still supports them on Windows):

-   Middle-click pastes the last selected text.
-   Middle-click on a scrollbar moves the scrollbar to that position without having to drag it.

</div>

</div>

<div id="compile-time-options" class="section">

# <a href="#toc-entry-255" class="toc-backref">Compile-time options</a>

There are some options which can only be changed at compile time, and some options which are used as the default for configurable options. To change these options, edit the appropriate source file in the src subdirectory. Look for a block of lines starting with \#define GEANY\_\*. Any definitions which are not listed here should not be changed.

<div class="admonition note">

Note

Most users should not need to change these options.

</div>

<div id="src-geany-h" class="section">

## <a href="#toc-entry-256" class="toc-backref">src/geany.h</a>

| Option                      | Description                                                                                                                                                                                                                                                                                         | Default  |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| GEANY_STRING_UNTITLED       | A string used as the default name for new files. Be aware that the string can be translated, so change it only if you know what you are doing.                                                                                                                                                      | untitled |
| GEANY_WINDOW_MINIMAL_WIDTH  | The minimal width of the main window.                                                                                                                                                                                                                                                               | 620      |
| GEANY_WINDOW_MINIMAL_HEIGHT | The minimal height of the main window.                                                                                                                                                                                                                                                              | 440      |
| GEANY_WINDOW_DEFAULT_WIDTH  | The default width of the main window at the first start.                                                                                                                                                                                                                                            | 900      |
| GEANY_WINDOW_DEFAULT_HEIGHT | The default height of the main window at the first start.                                                                                                                                                                                                                                           | 600      |
| **Windows specific**        |                                                                                                                                                                                                                                                                                                     |          |
| GEANY_USE_WIN32_DIALOG      | Set this to 1 if you want to use the default Windows file open and save dialogs instead GTK's file open and save dialogs. The default Windows file dialogs are missing some nice features like choosing a filetype or an encoding. *Do not touch this setting when building on a non-Win32 system.* | 0        |

</div>

<div id="project-h" class="section">

## <a href="#toc-entry-257" class="toc-backref">project.h</a>

| Option            | Description                                                                                                                                   | Default |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------|
| GEANY_PROJECT_EXT | The default filename extension for Geany project files. It is used when creating new projects and as filter mask for the project open dialog. | geany   |

</div>

<div id="filetypes-c" class="section">

## <a href="#toc-entry-258" class="toc-backref">filetypes.c</a>

| Option                      | Description                                                                     | Default |
|-----------------------------|---------------------------------------------------------------------------------|---------|
| GEANY_FILETYPE_SEARCH_LINES | The number of lines to search for the filetype with the extract filetype regex. | 2       |

</div>

<div id="editor-h" class="section">

## <a href="#toc-entry-259" class="toc-backref">editor.h</a>

| Option          | Description                                                                                               | Default                                      |
|-----------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------|
| GEANY_WORDCHARS | These characters define word boundaries when making selections and searching using word matching options. | a string with: a-z, A-Z, 0-9 and underscore. |

</div>

<div id="keyfile-c" class="section">

## <a href="#toc-entry-260" class="toc-backref">keyfile.c</a>

These are default settings that can be overridden in the <a href="#preferences" class="reference internal">Preferences</a> dialog.

| Option                         | Description                                                                                                       | Default        |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------|
| GEANY_MIN_SYMBOLLIST_CHARS     | How many characters you need to type to trigger the autocompletion list.                                          | 4              |
| GEANY_DISK_CHECK_TIMEOUT       | Time in seconds between checking a file for external changes.                                                     | 30             |
| GEANY_DEFAULT_TOOLS_MAKE       | The make tool. This can also include a path.                                                                      | "make"         |
| GEANY_DEFAULT_TOOLS_TERMINAL   | A terminal emulator command, see <a href="#terminal-emulators" class="reference internal">Terminal emulators</a>. | See below.     |
| GEANY_DEFAULT_TOOLS_BROWSER    | A web browser. This can also include a path.                                                                      | "firefox"      |
| GEANY_DEFAULT_TOOLS_PRINTCMD   | A printing tool. It should be able to accept and process plain text files. This can also include a path.          | "lpr"          |
| GEANY_DEFAULT_TOOLS_GREP       | A grep tool. It should be compatible with GNU grep. This can also include a path.                                 | "grep"         |
| GEANY_DEFAULT_MRU_LENGTH       | The length of the "Recent files" list.                                                                            | 10             |
| GEANY_DEFAULT_FONT_SYMBOL_LIST | The font used in sidebar to show symbols and open files.                                                          | "Sans 9"       |
| GEANY_DEFAULT_FONT_MSG_WINDOW  | The font used in the messages window.                                                                             | "Sans 9"       |
| GEANY_DEFAULT_FONT_EDITOR      | The font used in the editor window.                                                                               | "Monospace 10" |
| GEANY_TOGGLE_MARK              | A string which is used to mark a toggled comment.                                                                 | "\~ "          |
| GEANY_MAX_AUTOCOMPLETE_WORDS   | How many autocompletion suggestions should Geany provide.                                                         | 30             |
| GEANY_DEFAULT_FILETYPE_REGEX   | The default regex to extract filetypes from files.                                                                | See below.     |

The GEANY_DEFAULT_FILETYPE_REGEX default value is -\\\*-\\s\*(\[^\\s\]+)\\s\*-\\\*- which finds Emacs filetypes.

The GEANY_DEFAULT_TOOLS_TERMINAL default value on Windows is:

``` literal-block
cmd.exe /Q /C %c
```

and on any non-Windows system is:

``` literal-block
xterm -e "/bin/sh %c"
```

</div>

<div id="build-c" class="section">

## <a href="#toc-entry-261" class="toc-backref">build.c</a>

| Option                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                      | Default |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| GEANY_BUILD_ERR_HIGHLIGHT_MAX | Amount of build error indicators to be shown in the editor window. This affects the special coloring when Geany detects a compiler output line as an error message and then highlights the corresponding line in the source code. Usually only the first few messages are interesting because following errors are just after-effects. All errors in the Compiler window are parsed and unaffected by this value.                | 50      |
| PRINTBUILDCMDS                | Every time a build menu item priority calculation is run, print the state of the menu item table in the form of the table in <a href="#build-menu-configuration" class="reference internal">Build Menu Configuration</a>. May be useful to debug configuration file overloading. Warning produces a lot of output. Can also be enabled/disabled by the debugger by setting printbuildcmds to 1/0 overriding the compile setting. | FALSE   |

</div>

</div>

<div id="gnu-general-public-license" class="section">

# <a href="#toc-entry-262" class="toc-backref">GNU General Public License</a>

``` literal-block
            GNU GENERAL PUBLIC LICENSE
               Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Library General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

            GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

                NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

             END OF TERMS AND CONDITIONS

        How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year  name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Library General
Public License instead of this License.
```

</div>

<div id="license-for-scintilla-and-scite" class="section">

# <a href="#toc-entry-263" class="toc-backref">License for Scintilla and SciTE</a>

Copyright 1998-2003 by Neil Hodgson \<neilh(at)scintilla(dot)org\>

All Rights Reserved

Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation.

NEIL HODGSON DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL NEIL HODGSON BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

</div>

<div class="footer">

------------------------------------------------------------------------

<a href="geany.txt" class="reference external">View document source</a>. Generated on: 2025-07-06 13:04 UTC. Generated by <a href="https://docutils.sourceforge.io/" class="reference external">Docutils</a> from <a href="https://docutils.sourceforge.io/rst.html" class="reference external">reStructuredText</a> source.

</div>
