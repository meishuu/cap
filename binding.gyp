{
  'targets': [
    {
      'target_name': 'cap',
      'sources': [
        'src/binding.cc',
      ],
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
      ],
      'conditions': [
        [ 'OS=="win"', {
          'include_dirs': [
            'deps/npcap-sdk-1.03/Include',
          ],
          'defines': [
            'WPCAP',
          ],
          'conditions': [
            [ 'target_arch=="ia32"', {
              'link_settings': {
                'libraries': ['ws2_32.lib', '<(PRODUCT_DIR)/../../deps/npcap-sdk-1.03/Lib/wpcap.lib'],
              },
            }, {
              'link_settings': {
                'libraries': ['ws2_32.lib', '<(PRODUCT_DIR)/../../deps/npcap-sdk-1.03/Lib/x64/wpcap.lib'],
              },
            }],
          ],
        }, {
          # POSIX
          'link_settings': {
            'libraries': ['-lpcap'],
          },
        }],
      ],
    },
  ],
}