
IF (BUILD_GUI)
    PYSIDE_WRAP_RC(SpreadsheetAliasManager_QRC_SRCS Resources/SpreadsheetAliasManager.qrc)
ENDIF (BUILD_GUI)

SET(SpreadsheetAliasManager_SRCS
    Init.py
    InitGui.py
    SpreadsheetAliasManager.py
    SpreadsheetAliasManagerGui.py
)
SOURCE_GROUP("" FILES ${SpreadsheetAliasManager_SRCS})

ADD_CUSTOM_TARGET(SpreadsheetAliasManager ALL
    SOURCES ${SpreadsheetAliasManager_SRCS} ${SpreadsheetAliasManager_QRC_SRCS}
)

fc_copy_sources(SpreadsheetAliasManager "${CMAKE_BINARY_DIR}/Mod/SpreadsheetAliasManager" ${SpreadsheetAliasManager_SRCS})

IF (BUILD_GUI)
    fc_target_copy_resource(SpreadsheetAliasManager
        ${CMAKE_CURRENT_BINARY_DIR}
        ${CMAKE_BINARY_DIR}/Mod/SpreadsheetAliasManager
        SpreadsheetAliasManager_rc.py)
ENDIF (BUILD_GUI)

INSTALL(
    FILES
        ${SpreadsheetAliasManager_SRCS}
        ${SpreadsheetAliasManager_QRC_SRCS}
    DESTINATION
        Mod/SpreadsheetAliasManager
)

SET(SpreadsheetAliasManagerGuiIcon_SVG
    Resources/icons/SpreadsheetAliasManagerWorkbench.svg
)

fc_copy_sources(SpreadsheetAliasManager "${CMAKE_BINARY_DIR}/Mod/SpreadsheetAliasManager" ${SpreadsheetAliasManagerGuiIcon_SVG})
INSTALL(FILES ${SpreadsheetAliasManagerGuiIcon_SVG} DESTINATION "Mod/SpreadsheetAliasManager/Resources/icons")
