custom_target('atom_dark',
  build_by_default : true,
  input : 'atom.less',
  output : 'colors_dark.less',
  command : [subtempl, dark, '@INPUT@', '@OUTPUT@']
)

custom_target('atom_light',
  build_by_default : true,
  input : 'atom.less',
  output : 'colors_light.less',
  command : [subtempl, light, '@INPUT@', '@OUTPUT@']
)
