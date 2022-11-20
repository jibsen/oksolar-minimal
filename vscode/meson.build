custom_target('vscode_dark',
  build_by_default : true,
  input : 'vscode.json',
  output : 'oksolar_minimal_dark.json',
  command : [subtempl, dark, '@INPUT@', '@OUTPUT@']
)

custom_target('vscode_light',
  build_by_default : true,
  input : 'vscode.json',
  output : 'oksolar_minimal_light.json',
  command : [subtempl, light, '@INPUT@', '@OUTPUT@']
)
