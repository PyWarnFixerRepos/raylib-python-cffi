from enum import IntEnum

class ConfigFlags(IntEnum):
    FLAG_VSYNC_HINT = 64
    FLAG_FULLSCREEN_MODE = 2
    FLAG_WINDOW_RESIZABLE = 4
    FLAG_WINDOW_UNDECORATED = 8
    FLAG_WINDOW_HIDDEN = 128
    FLAG_WINDOW_MINIMIZED = 512
    FLAG_WINDOW_MAXIMIZED = 1024
    FLAG_WINDOW_UNFOCUSED = 2048
    FLAG_WINDOW_TOPMOST = 4096
    FLAG_WINDOW_ALWAYS_RUN = 256
    FLAG_WINDOW_TRANSPARENT = 16
    FLAG_WINDOW_HIGHDPI = 8192
    FLAG_MSAA_4X_HINT = 32
    FLAG_INTERLACED_HINT = 65536

class TraceLogLevel(IntEnum):
    LOG_ALL = 0
    LOG_TRACE = 1
    LOG_DEBUG = 2
    LOG_INFO = 3
    LOG_WARNING = 4
    LOG_ERROR = 5
    LOG_FATAL = 6
    LOG_NONE = 7

class KeyboardKey(IntEnum):
    KEY_NULL = 0
    KEY_APOSTROPHE = 39
    KEY_COMMA = 44
    KEY_MINUS = 45
    KEY_PERIOD = 46
    KEY_SLASH = 47
    KEY_ZERO = 48
    KEY_ONE = 49
    KEY_TWO = 50
    KEY_THREE = 51
    KEY_FOUR = 52
    KEY_FIVE = 53
    KEY_SIX = 54
    KEY_SEVEN = 55
    KEY_EIGHT = 56
    KEY_NINE = 57
    KEY_SEMICOLON = 59
    KEY_EQUAL = 61
    KEY_A = 65
    KEY_B = 66
    KEY_C = 67
    KEY_D = 68
    KEY_E = 69
    KEY_F = 70
    KEY_G = 71
    KEY_H = 72
    KEY_I = 73
    KEY_J = 74
    KEY_K = 75
    KEY_L = 76
    KEY_M = 77
    KEY_N = 78
    KEY_O = 79
    KEY_P = 80
    KEY_Q = 81
    KEY_R = 82
    KEY_S = 83
    KEY_T = 84
    KEY_U = 85
    KEY_V = 86
    KEY_W = 87
    KEY_X = 88
    KEY_Y = 89
    KEY_Z = 90
    KEY_LEFT_BRACKET = 91
    KEY_BACKSLASH = 92
    KEY_RIGHT_BRACKET = 93
    KEY_GRAVE = 96
    KEY_SPACE = 32
    KEY_ESCAPE = 256
    KEY_ENTER = 257
    KEY_TAB = 258
    KEY_BACKSPACE = 259
    KEY_INSERT = 260
    KEY_DELETE = 261
    KEY_RIGHT = 262
    KEY_LEFT = 263
    KEY_DOWN = 264
    KEY_UP = 265
    KEY_PAGE_UP = 266
    KEY_PAGE_DOWN = 267
    KEY_HOME = 268
    KEY_END = 269
    KEY_CAPS_LOCK = 280
    KEY_SCROLL_LOCK = 281
    KEY_NUM_LOCK = 282
    KEY_PRINT_SCREEN = 283
    KEY_PAUSE = 284
    KEY_F1 = 290
    KEY_F2 = 291
    KEY_F3 = 292
    KEY_F4 = 293
    KEY_F5 = 294
    KEY_F6 = 295
    KEY_F7 = 296
    KEY_F8 = 297
    KEY_F9 = 298
    KEY_F10 = 299
    KEY_F11 = 300
    KEY_F12 = 301
    KEY_LEFT_SHIFT = 340
    KEY_LEFT_CONTROL = 341
    KEY_LEFT_ALT = 342
    KEY_LEFT_SUPER = 343
    KEY_RIGHT_SHIFT = 344
    KEY_RIGHT_CONTROL = 345
    KEY_RIGHT_ALT = 346
    KEY_RIGHT_SUPER = 347
    KEY_KB_MENU = 348
    KEY_KP_0 = 320
    KEY_KP_1 = 321
    KEY_KP_2 = 322
    KEY_KP_3 = 323
    KEY_KP_4 = 324
    KEY_KP_5 = 325
    KEY_KP_6 = 326
    KEY_KP_7 = 327
    KEY_KP_8 = 328
    KEY_KP_9 = 329
    KEY_KP_DECIMAL = 330
    KEY_KP_DIVIDE = 331
    KEY_KP_MULTIPLY = 332
    KEY_KP_SUBTRACT = 333
    KEY_KP_ADD = 334
    KEY_KP_ENTER = 335
    KEY_KP_EQUAL = 336
    KEY_BACK = 4
    KEY_MENU = 82
    KEY_VOLUME_UP = 24
    KEY_VOLUME_DOWN = 25

class MouseButton(IntEnum):
    MOUSE_BUTTON_LEFT = 0
    MOUSE_BUTTON_RIGHT = 1
    MOUSE_BUTTON_MIDDLE = 2
    MOUSE_BUTTON_SIDE = 3
    MOUSE_BUTTON_EXTRA = 4
    MOUSE_BUTTON_FORWARD = 5
    MOUSE_BUTTON_BACK = 6

class MouseCursor(IntEnum):
    MOUSE_CURSOR_DEFAULT = 0
    MOUSE_CURSOR_ARROW = 1
    MOUSE_CURSOR_IBEAM = 2
    MOUSE_CURSOR_CROSSHAIR = 3
    MOUSE_CURSOR_POINTING_HAND = 4
    MOUSE_CURSOR_RESIZE_EW = 5
    MOUSE_CURSOR_RESIZE_NS = 6
    MOUSE_CURSOR_RESIZE_NWSE = 7
    MOUSE_CURSOR_RESIZE_NESW = 8
    MOUSE_CURSOR_RESIZE_ALL = 9
    MOUSE_CURSOR_NOT_ALLOWED = 10

class GamepadButton(IntEnum):
    GAMEPAD_BUTTON_UNKNOWN = 0
    GAMEPAD_BUTTON_LEFT_FACE_UP = 1
    GAMEPAD_BUTTON_LEFT_FACE_RIGHT = 2
    GAMEPAD_BUTTON_LEFT_FACE_DOWN = 3
    GAMEPAD_BUTTON_LEFT_FACE_LEFT = 4
    GAMEPAD_BUTTON_RIGHT_FACE_UP = 5
    GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = 6
    GAMEPAD_BUTTON_RIGHT_FACE_DOWN = 7
    GAMEPAD_BUTTON_RIGHT_FACE_LEFT = 8
    GAMEPAD_BUTTON_LEFT_TRIGGER_1 = 9
    GAMEPAD_BUTTON_LEFT_TRIGGER_2 = 10
    GAMEPAD_BUTTON_RIGHT_TRIGGER_1 = 11
    GAMEPAD_BUTTON_RIGHT_TRIGGER_2 = 12
    GAMEPAD_BUTTON_MIDDLE_LEFT = 13
    GAMEPAD_BUTTON_MIDDLE = 14
    GAMEPAD_BUTTON_MIDDLE_RIGHT = 15
    GAMEPAD_BUTTON_LEFT_THUMB = 16
    GAMEPAD_BUTTON_RIGHT_THUMB = 17

class GamepadAxis(IntEnum):
    GAMEPAD_AXIS_LEFT_X = 0
    GAMEPAD_AXIS_LEFT_Y = 1
    GAMEPAD_AXIS_RIGHT_X = 2
    GAMEPAD_AXIS_RIGHT_Y = 3
    GAMEPAD_AXIS_LEFT_TRIGGER = 4
    GAMEPAD_AXIS_RIGHT_TRIGGER = 5

class MaterialMapIndex(IntEnum):
    MATERIAL_MAP_ALBEDO = 0
    MATERIAL_MAP_METALNESS = 1
    MATERIAL_MAP_NORMAL = 2
    MATERIAL_MAP_ROUGHNESS = 3
    MATERIAL_MAP_OCCLUSION = 4
    MATERIAL_MAP_EMISSION = 5
    MATERIAL_MAP_HEIGHT = 6
    MATERIAL_MAP_CUBEMAP = 7
    MATERIAL_MAP_IRRADIANCE = 8
    MATERIAL_MAP_PREFILTER = 9
    MATERIAL_MAP_BRDF = 10

class ShaderLocationIndex(IntEnum):
    SHADER_LOC_VERTEX_POSITION = 0
    SHADER_LOC_VERTEX_TEXCOORD01 = 1
    SHADER_LOC_VERTEX_TEXCOORD02 = 2
    SHADER_LOC_VERTEX_NORMAL = 3
    SHADER_LOC_VERTEX_TANGENT = 4
    SHADER_LOC_VERTEX_COLOR = 5
    SHADER_LOC_MATRIX_MVP = 6
    SHADER_LOC_MATRIX_VIEW = 7
    SHADER_LOC_MATRIX_PROJECTION = 8
    SHADER_LOC_MATRIX_MODEL = 9
    SHADER_LOC_MATRIX_NORMAL = 10
    SHADER_LOC_VECTOR_VIEW = 11
    SHADER_LOC_COLOR_DIFFUSE = 12
    SHADER_LOC_COLOR_SPECULAR = 13
    SHADER_LOC_COLOR_AMBIENT = 14
    SHADER_LOC_MAP_ALBEDO = 15
    SHADER_LOC_MAP_METALNESS = 16
    SHADER_LOC_MAP_NORMAL = 17
    SHADER_LOC_MAP_ROUGHNESS = 18
    SHADER_LOC_MAP_OCCLUSION = 19
    SHADER_LOC_MAP_EMISSION = 20
    SHADER_LOC_MAP_HEIGHT = 21
    SHADER_LOC_MAP_CUBEMAP = 22
    SHADER_LOC_MAP_IRRADIANCE = 23
    SHADER_LOC_MAP_PREFILTER = 24
    SHADER_LOC_MAP_BRDF = 25

class ShaderUniformDataType(IntEnum):
    SHADER_UNIFORM_FLOAT = 0
    SHADER_UNIFORM_VEC2 = 1
    SHADER_UNIFORM_VEC3 = 2
    SHADER_UNIFORM_VEC4 = 3
    SHADER_UNIFORM_INT = 4
    SHADER_UNIFORM_IVEC2 = 5
    SHADER_UNIFORM_IVEC3 = 6
    SHADER_UNIFORM_IVEC4 = 7
    SHADER_UNIFORM_SAMPLER2D = 8

class ShaderAttributeDataType(IntEnum):
    SHADER_ATTRIB_FLOAT = 0
    SHADER_ATTRIB_VEC2 = 1
    SHADER_ATTRIB_VEC3 = 2
    SHADER_ATTRIB_VEC4 = 3

class PixelFormat(IntEnum):
    PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = 1
    PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = 2
    PIXELFORMAT_UNCOMPRESSED_R5G6B5 = 3
    PIXELFORMAT_UNCOMPRESSED_R8G8B8 = 4
    PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = 5
    PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = 6
    PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = 7
    PIXELFORMAT_UNCOMPRESSED_R32 = 8
    PIXELFORMAT_UNCOMPRESSED_R32G32B32 = 9
    PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = 10
    PIXELFORMAT_COMPRESSED_DXT1_RGB = 11
    PIXELFORMAT_COMPRESSED_DXT1_RGBA = 12
    PIXELFORMAT_COMPRESSED_DXT3_RGBA = 13
    PIXELFORMAT_COMPRESSED_DXT5_RGBA = 14
    PIXELFORMAT_COMPRESSED_ETC1_RGB = 15
    PIXELFORMAT_COMPRESSED_ETC2_RGB = 16
    PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 17
    PIXELFORMAT_COMPRESSED_PVRT_RGB = 18
    PIXELFORMAT_COMPRESSED_PVRT_RGBA = 19
    PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 20
    PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 21

class TextureFilter(IntEnum):
    TEXTURE_FILTER_POINT = 0
    TEXTURE_FILTER_BILINEAR = 1
    TEXTURE_FILTER_TRILINEAR = 2
    TEXTURE_FILTER_ANISOTROPIC_4X = 3
    TEXTURE_FILTER_ANISOTROPIC_8X = 4
    TEXTURE_FILTER_ANISOTROPIC_16X = 5

class TextureWrap(IntEnum):
    TEXTURE_WRAP_REPEAT = 0
    TEXTURE_WRAP_CLAMP = 1
    TEXTURE_WRAP_MIRROR_REPEAT = 2
    TEXTURE_WRAP_MIRROR_CLAMP = 3

class CubemapLayout(IntEnum):
    CUBEMAP_LAYOUT_AUTO_DETECT = 0
    CUBEMAP_LAYOUT_LINE_VERTICAL = 1
    CUBEMAP_LAYOUT_LINE_HORIZONTAL = 2
    CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = 3
    CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = 4
    CUBEMAP_LAYOUT_PANORAMA = 5

class FontType(IntEnum):
    FONT_DEFAULT = 0
    FONT_BITMAP = 1
    FONT_SDF = 2

class BlendMode(IntEnum):
    BLEND_ALPHA = 0
    BLEND_ADDITIVE = 1
    BLEND_MULTIPLIED = 2
    BLEND_ADD_COLORS = 3
    BLEND_SUBTRACT_COLORS = 4
    BLEND_CUSTOM = 5

class Gesture(IntEnum):
    GESTURE_NONE = 0
    GESTURE_TAP = 1
    GESTURE_DOUBLETAP = 2
    GESTURE_HOLD = 4
    GESTURE_DRAG = 8
    GESTURE_SWIPE_RIGHT = 16
    GESTURE_SWIPE_LEFT = 32
    GESTURE_SWIPE_UP = 64
    GESTURE_SWIPE_DOWN = 128
    GESTURE_PINCH_IN = 256
    GESTURE_PINCH_OUT = 512

class CameraMode(IntEnum):
    CAMERA_CUSTOM = 0
    CAMERA_FREE = 1
    CAMERA_ORBITAL = 2
    CAMERA_FIRST_PERSON = 3
    CAMERA_THIRD_PERSON = 4

class CameraProjection(IntEnum):
    CAMERA_PERSPECTIVE = 0
    CAMERA_ORTHOGRAPHIC = 1

class NPatchLayout(IntEnum):
    NPATCH_NINE_PATCH = 0
    NPATCH_THREE_PATCH_VERTICAL = 1
    NPATCH_THREE_PATCH_HORIZONTAL = 2

class GuiControlState(IntEnum):
    GUI_STATE_NORMAL = 0
    GUI_STATE_FOCUSED = 1
    GUI_STATE_PRESSED = 2
    GUI_STATE_DISABLED = 3

class GuiTextAlignment(IntEnum):
    GUI_TEXT_ALIGN_LEFT = 0
    GUI_TEXT_ALIGN_CENTER = 1
    GUI_TEXT_ALIGN_RIGHT = 2

class GuiControl(IntEnum):
    DEFAULT = 0
    LABEL = 1
    BUTTON = 2
    TOGGLE = 3
    SLIDER = 4
    PROGRESSBAR = 5
    CHECKBOX = 6
    COMBOBOX = 7
    DROPDOWNBOX = 8
    TEXTBOX = 9
    VALUEBOX = 10
    SPINNER = 11
    LISTVIEW = 12
    COLORPICKER = 13
    SCROLLBAR = 14
    STATUSBAR = 15

class GuiControlProperty(IntEnum):
    BORDER_COLOR_NORMAL = 0
    BASE_COLOR_NORMAL = 1
    TEXT_COLOR_NORMAL = 2
    BORDER_COLOR_FOCUSED = 3
    BASE_COLOR_FOCUSED = 4
    TEXT_COLOR_FOCUSED = 5
    BORDER_COLOR_PRESSED = 6
    BASE_COLOR_PRESSED = 7
    TEXT_COLOR_PRESSED = 8
    BORDER_COLOR_DISABLED = 9
    BASE_COLOR_DISABLED = 10
    TEXT_COLOR_DISABLED = 11
    BORDER_WIDTH = 12
    TEXT_PADDING = 13
    TEXT_ALIGNMENT = 14
    RESERVED = 15

class GuiDefaultProperty(IntEnum):
    TEXT_SIZE = 16
    TEXT_SPACING = 17
    LINE_COLOR = 18
    BACKGROUND_COLOR = 19

class GuiToggleProperty(IntEnum):
    GROUP_PADDING = 16

class GuiSliderProperty(IntEnum):
    SLIDER_WIDTH = 16
    SLIDER_PADDING = 17

class GuiProgressBarProperty(IntEnum):
    PROGRESS_PADDING = 16

class GuiCheckBoxProperty(IntEnum):
    CHECK_PADDING = 16

class GuiComboBoxProperty(IntEnum):
    COMBO_BUTTON_WIDTH = 16
    COMBO_BUTTON_PADDING = 17

class GuiDropdownBoxProperty(IntEnum):
    ARROW_PADDING = 16
    DROPDOWN_ITEMS_PADDING = 17

class GuiTextBoxProperty(IntEnum):
    TEXT_INNER_PADDING = 16
    TEXT_LINES_PADDING = 17
    COLOR_SELECTED_FG = 18
    COLOR_SELECTED_BG = 19

class GuiSpinnerProperty(IntEnum):
    SPIN_BUTTON_WIDTH = 16
    SPIN_BUTTON_PADDING = 17

class GuiScrollBarProperty(IntEnum):
    ARROWS_SIZE = 16
    ARROWS_VISIBLE = 17
    SCROLL_SLIDER_PADDING = 18
    SCROLL_SLIDER_SIZE = 19
    SCROLL_PADDING = 20
    SCROLL_SPEED = 21

class GuiScrollBarSide(IntEnum):
    SCROLLBAR_LEFT_SIDE = 0
    SCROLLBAR_RIGHT_SIDE = 1

class GuiListViewProperty(IntEnum):
    LIST_ITEMS_HEIGHT = 16
    LIST_ITEMS_PADDING = 17
    SCROLLBAR_WIDTH = 18
    SCROLLBAR_SIDE = 19

class GuiColorPickerProperty(IntEnum):
    COLOR_SELECTOR_SIZE = 16
    HUEBAR_WIDTH = 17
    HUEBAR_PADDING = 18
    HUEBAR_SELECTOR_HEIGHT = 19
    HUEBAR_SELECTOR_OVERFLOW = 20

class guiIconName(IntEnum):
    RICON_NONE = 0
    RICON_FOLDER_FILE_OPEN = 1
    RICON_FILE_SAVE_CLASSIC = 2
    RICON_FOLDER_OPEN = 3
    RICON_FOLDER_SAVE = 4
    RICON_FILE_OPEN = 5
    RICON_FILE_SAVE = 6
    RICON_FILE_EXPORT = 7
    RICON_FILE_NEW = 8
    RICON_FILE_DELETE = 9
    RICON_FILETYPE_TEXT = 10
    RICON_FILETYPE_AUDIO = 11
    RICON_FILETYPE_IMAGE = 12
    RICON_FILETYPE_PLAY = 13
    RICON_FILETYPE_VIDEO = 14
    RICON_FILETYPE_INFO = 15
    RICON_FILE_COPY = 16
    RICON_FILE_CUT = 17
    RICON_FILE_PASTE = 18
    RICON_CURSOR_HAND = 19
    RICON_CURSOR_POINTER = 20
    RICON_CURSOR_CLASSIC = 21
    RICON_PENCIL = 22
    RICON_PENCIL_BIG = 23
    RICON_BRUSH_CLASSIC = 24
    RICON_BRUSH_PAINTER = 25
    RICON_WATER_DROP = 26
    RICON_COLOR_PICKER = 27
    RICON_RUBBER = 28
    RICON_COLOR_BUCKET = 29
    RICON_TEXT_T = 30
    RICON_TEXT_A = 31
    RICON_SCALE = 32
    RICON_RESIZE = 33
    RICON_FILTER_POINT = 34
    RICON_FILTER_BILINEAR = 35
    RICON_CROP = 36
    RICON_CROP_ALPHA = 37
    RICON_SQUARE_TOGGLE = 38
    RICON_SYMMETRY = 39
    RICON_SYMMETRY_HORIZONTAL = 40
    RICON_SYMMETRY_VERTICAL = 41
    RICON_LENS = 42
    RICON_LENS_BIG = 43
    RICON_EYE_ON = 44
    RICON_EYE_OFF = 45
    RICON_FILTER_TOP = 46
    RICON_FILTER = 47
    RICON_TARGET_POINT = 48
    RICON_TARGET_SMALL = 49
    RICON_TARGET_BIG = 50
    RICON_TARGET_MOVE = 51
    RICON_CURSOR_MOVE = 52
    RICON_CURSOR_SCALE = 53
    RICON_CURSOR_SCALE_RIGHT = 54
    RICON_CURSOR_SCALE_LEFT = 55
    RICON_UNDO = 56
    RICON_REDO = 57
    RICON_REREDO = 58
    RICON_MUTATE = 59
    RICON_ROTATE = 60
    RICON_REPEAT = 61
    RICON_SHUFFLE = 62
    RICON_EMPTYBOX = 63
    RICON_TARGET = 64
    RICON_TARGET_SMALL_FILL = 65
    RICON_TARGET_BIG_FILL = 66
    RICON_TARGET_MOVE_FILL = 67
    RICON_CURSOR_MOVE_FILL = 68
    RICON_CURSOR_SCALE_FILL = 69
    RICON_CURSOR_SCALE_RIGHT_FILL = 70
    RICON_CURSOR_SCALE_LEFT_FILL = 71
    RICON_UNDO_FILL = 72
    RICON_REDO_FILL = 73
    RICON_REREDO_FILL = 74
    RICON_MUTATE_FILL = 75
    RICON_ROTATE_FILL = 76
    RICON_REPEAT_FILL = 77
    RICON_SHUFFLE_FILL = 78
    RICON_EMPTYBOX_SMALL = 79
    RICON_BOX = 80
    RICON_BOX_TOP = 81
    RICON_BOX_TOP_RIGHT = 82
    RICON_BOX_RIGHT = 83
    RICON_BOX_BOTTOM_RIGHT = 84
    RICON_BOX_BOTTOM = 85
    RICON_BOX_BOTTOM_LEFT = 86
    RICON_BOX_LEFT = 87
    RICON_BOX_TOP_LEFT = 88
    RICON_BOX_CENTER = 89
    RICON_BOX_CIRCLE_MASK = 90
    RICON_POT = 91
    RICON_ALPHA_MULTIPLY = 92
    RICON_ALPHA_CLEAR = 93
    RICON_DITHERING = 94
    RICON_MIPMAPS = 95
    RICON_BOX_GRID = 96
    RICON_GRID = 97
    RICON_BOX_CORNERS_SMALL = 98
    RICON_BOX_CORNERS_BIG = 99
    RICON_FOUR_BOXES = 100
    RICON_GRID_FILL = 101
    RICON_BOX_MULTISIZE = 102
    RICON_ZOOM_SMALL = 103
    RICON_ZOOM_MEDIUM = 104
    RICON_ZOOM_BIG = 105
    RICON_ZOOM_ALL = 106
    RICON_ZOOM_CENTER = 107
    RICON_BOX_DOTS_SMALL = 108
    RICON_BOX_DOTS_BIG = 109
    RICON_BOX_CONCENTRIC = 110
    RICON_BOX_GRID_BIG = 111
    RICON_OK_TICK = 112
    RICON_CROSS = 113
    RICON_ARROW_LEFT = 114
    RICON_ARROW_RIGHT = 115
    RICON_ARROW_DOWN = 116
    RICON_ARROW_UP = 117
    RICON_ARROW_LEFT_FILL = 118
    RICON_ARROW_RIGHT_FILL = 119
    RICON_ARROW_DOWN_FILL = 120
    RICON_ARROW_UP_FILL = 121
    RICON_AUDIO = 122
    RICON_FX = 123
    RICON_WAVE = 124
    RICON_WAVE_SINUS = 125
    RICON_WAVE_SQUARE = 126
    RICON_WAVE_TRIANGULAR = 127
    RICON_CROSS_SMALL = 128
    RICON_PLAYER_PREVIOUS = 129
    RICON_PLAYER_PLAY_BACK = 130
    RICON_PLAYER_PLAY = 131
    RICON_PLAYER_PAUSE = 132
    RICON_PLAYER_STOP = 133
    RICON_PLAYER_NEXT = 134
    RICON_PLAYER_RECORD = 135
    RICON_MAGNET = 136
    RICON_LOCK_CLOSE = 137
    RICON_LOCK_OPEN = 138
    RICON_CLOCK = 139
    RICON_TOOLS = 140
    RICON_GEAR = 141
    RICON_GEAR_BIG = 142
    RICON_BIN = 143
    RICON_HAND_POINTER = 144
    RICON_LASER = 145
    RICON_COIN = 146
    RICON_EXPLOSION = 147
    RICON_1UP = 148
    RICON_PLAYER = 149
    RICON_PLAYER_JUMP = 150
    RICON_KEY = 151
    RICON_DEMON = 152
    RICON_TEXT_POPUP = 153
    RICON_GEAR_EX = 154
    RICON_CRACK = 155
    RICON_CRACK_POINTS = 156
    RICON_STAR = 157
    RICON_DOOR = 158
    RICON_EXIT = 159
    RICON_MODE_2D = 160
    RICON_MODE_3D = 161
    RICON_CUBE = 162
    RICON_CUBE_FACE_TOP = 163
    RICON_CUBE_FACE_LEFT = 164
    RICON_CUBE_FACE_FRONT = 165
    RICON_CUBE_FACE_BOTTOM = 166
    RICON_CUBE_FACE_RIGHT = 167
    RICON_CUBE_FACE_BACK = 168
    RICON_CAMERA = 169
    RICON_SPECIAL = 170
    RICON_LINK_NET = 171
    RICON_LINK_BOXES = 172
    RICON_LINK_MULTI = 173
    RICON_LINK = 174
    RICON_LINK_BROKE = 175
    RICON_TEXT_NOTES = 176
    RICON_NOTEBOOK = 177
    RICON_SUITCASE = 178
    RICON_SUITCASE_ZIP = 179
    RICON_MAILBOX = 180
    RICON_MONITOR = 181
    RICON_PRINTER = 182
    RICON_PHOTO_CAMERA = 183
    RICON_PHOTO_CAMERA_FLASH = 184
    RICON_HOUSE = 185
    RICON_HEART = 186
    RICON_CORNER = 187
    RICON_VERTICAL_BARS = 188
    RICON_VERTICAL_BARS_FILL = 189
    RICON_LIFE_BARS = 190
    RICON_INFO = 191
    RICON_CROSSLINE = 192
    RICON_HELP = 193
    RICON_FILETYPE_ALPHA = 194
    RICON_FILETYPE_HOME = 195
    RICON_LAYERS_VISIBLE = 196
    RICON_LAYERS = 197
    RICON_WINDOW = 198
    RICON_HIDPI = 199
    RICON_200 = 200
    RICON_201 = 201
    RICON_202 = 202
    RICON_203 = 203
    RICON_204 = 204
    RICON_205 = 205
    RICON_206 = 206
    RICON_207 = 207
    RICON_208 = 208
    RICON_209 = 209
    RICON_210 = 210
    RICON_211 = 211
    RICON_212 = 212
    RICON_213 = 213
    RICON_214 = 214
    RICON_215 = 215
    RICON_216 = 216
    RICON_217 = 217
    RICON_218 = 218
    RICON_219 = 219
    RICON_220 = 220
    RICON_221 = 221
    RICON_222 = 222
    RICON_223 = 223
    RICON_224 = 224
    RICON_225 = 225
    RICON_226 = 226
    RICON_227 = 227
    RICON_228 = 228
    RICON_229 = 229
    RICON_230 = 230
    RICON_231 = 231
    RICON_232 = 232
    RICON_233 = 233
    RICON_234 = 234
    RICON_235 = 235
    RICON_236 = 236
    RICON_237 = 237
    RICON_238 = 238
    RICON_239 = 239
    RICON_240 = 240
    RICON_241 = 241
    RICON_242 = 242
    RICON_243 = 243
    RICON_244 = 244
    RICON_245 = 245
    RICON_246 = 246
    RICON_247 = 247
    RICON_248 = 248
    RICON_249 = 249
    RICON_250 = 250
    RICON_251 = 251
    RICON_252 = 252
    RICON_253 = 253
    RICON_254 = 254
    RICON_255 = 255
