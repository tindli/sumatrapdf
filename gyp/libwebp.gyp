{
    'targets': [
        {
            'target_name': 'libwebp',
            'type': 'static_library',
            'include_dirs': [
                "../ext/libwebp",
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    "../ext/libwebp",
                ],
            },
            'msvs_disabled_warnings': [],
            'sources': [
                "../ext/libwebp/dec/alpha.c",
                "../ext/libwebp/dec/alphai.h",
                "../ext/libwebp/dec/buffer.c",
                "../ext/libwebp/dec/decode_vp8.h",
                "../ext/libwebp/dec/frame.c",
                "../ext/libwebp/dec/idec.c",
                "../ext/libwebp/dec/io.c",
                "../ext/libwebp/dec/quant.c",
                "../ext/libwebp/dec/tree.c",
                "../ext/libwebp/dec/vp8.c",
                "../ext/libwebp/dec/vp8i.h",
                "../ext/libwebp/dec/vp8l.c",
                "../ext/libwebp/dec/vp8li.h",
                "../ext/libwebp/dec/webp.c",
                "../ext/libwebp/dec/webpi.h",

                "../ext/libwebp/dsp/alpha_processing.c",
                "../ext/libwebp/dsp/alpha_processing_sse2.c",
                "../ext/libwebp/dsp/cpu.c",
                "../ext/libwebp/dsp/dec.c",
                "../ext/libwebp/dsp/dec_clip_tables.c",
                "../ext/libwebp/dsp/dec_sse2.c",
                "../ext/libwebp/dsp/dsp.h",
                "../ext/libwebp/dsp/lossless.c",
                "../ext/libwebp/dsp/lossless.h",
                "../ext/libwebp/dsp/lossless_sse2.c",
                "../ext/libwebp/dsp/upsampling.c",
                "../ext/libwebp/dsp/upsampling_sse2.c",
                "../ext/libwebp/dsp/yuv.c",
                "../ext/libwebp/dsp/yuv.h",
                "../ext/libwebp/dsp/yuv_sse2.c",
                "../ext/libwebp/dsp/yuv_tables_sse2.h",

                "../ext/libwebp/utils/bit_reader.c",
                "../ext/libwebp/utils/bit_reader.h",
                "../ext/libwebp/utils/color_cache.c",
                "../ext/libwebp/utils/color_cache.h",
                "../ext/libwebp/utils/endian_inl.h",
                "../ext/libwebp/utils/filters.c",
                "../ext/libwebp/utils/filters.h",
                "../ext/libwebp/utils/huffman.c",
                "../ext/libwebp/utils/huffman.h",
                "../ext/libwebp/utils/quant_levels_dec.c",
                "../ext/libwebp/utils/quant_levels_dec.h",
                "../ext/libwebp/utils/random.c",
                "../ext/libwebp/utils/random.h",
                "../ext/libwebp/utils/rescaler.c",
                "../ext/libwebp/utils/rescaler.h",
                "../ext/libwebp/utils/thread.c",
                "../ext/libwebp/utils/thread.h",
                "../ext/libwebp/utils/utils.c",
                "../ext/libwebp/utils/utils.h",

                "../ext/libwebp/webp/decode.h",
                "../ext/libwebp/webp/demux.h",
                "../ext/libwebp/webp/encode.h",
                "../ext/libwebp/webp/format_constants.h",
                "../ext/libwebp/webp/mux.h",
                "../ext/libwebp/webp/mux_types.h",
                "../ext/libwebp/webp/types.h",
            ],
        }
    ],
}
