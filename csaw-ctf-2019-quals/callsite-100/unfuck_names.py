shit = """
0x400448 _init
0x400460 sub_400460
0x400468 sub_400468
0x400470 j_memmove
0x400478 j_rawmemchr
0x400480 j_memcpy
0x400488 sub_400488
0x400490 sub_400490
0x400498 j___atomic_and_fetch_16
0x4004a0 j_strchrnul
0x4004a8 j___memchr
0x4004b0 j_strstr
0x4004b8 j_strncmp
0x4004c0 sub_4004c0
0x4004c8 j_wmemcmp
0x4004d0 j_strcasecmp_l
0x4004d8 j_memset
0x4004e0 sub_4004e0
0x4004e8 j_strcmp
0x4004f0 sub_4004f0
0x4004f8 j_mempcpy
0x400500 j___atomic_exchange_16
0x400508 j_strncasecmp_l
0x400510 j_strspn
0x400518 j_strlen
0x400520 j_index
0x400528 sub_400528
0x400530 sub_400530
0x400531 __malloc_assert.constprop.13
0x400587 __gconv_release_step.part.1
0x4005aa sub_4005aa
0x4005d0 fini
0x400600 main
0x4006c0 init_cacheinfo
0x400b50 _start
0x400b80 sub_400b80
0x400b90 sub_400b90
0x400bc0 _dl_init_paths
0x400c00 sub_400c00
0x400c40 sub_400c40
0x400c70 sub_400c70
0x400d30 sub_400d30
0x400d60 fips_enabled_p
0x400eb0 crypt_r
0x401090 fcrypt
0x401150 __md5_crypt_r
0x401870 __md5_crypt
0x4018e0 __sha256_crypt_r
0x402580 __sha256_crypt
0x4025f0 __sha512_crypt_r
0x403460 __sha512_crypt
0x4034d0 _ufc_doit_r
0x4035d0 _ufc_setup_salt_r.part.0
0x403aa0 __init_des_r
0x4040b0 _ufc_setup_salt_r
0x404170 _ufc_mk_keytab_r
0x404390 _ufc_dofinalperm_r
0x404560 _ufc_output_conversion_r
0x404820 encrypt_r
0x404b30 setkey_r
0x404d40 setkey
0x404f60 __b64_from_24bit
0x404fc0 __md5_init_ctx
0x404ff0 __md5_read_ctx
0x405010 __md5_process_block
0x405780 __md5_finish_ctx
0x405850 __md5_process_bytes
0x405ab0 __md5_buffer
0x405d20 __md5_stream
0x405ee0 __sha256_init_ctx
0x405f10 __sha256_process_block
0x4062d0 __sha256_finish_ctx
0x4063a0 __sha256_process_bytes
0x406600 __sha512_init_ctx
0x406640 __sha512_process_block
0x406a10 __sha512_finish_ctx
0x406b20 __sha512_process_bytes
0x406d60 get_common_indeces.constprop.1
0x406fd0 __libc_start_main
0x407650 __libc_check_standard_fds
0x4077e0 __libc_setup_tls
0x407a30 __libc_csu_init
0x407ad0 __libc_csu_fini
0x407b20 __assert_fail_base
0x407c80 __assert_fail
0x407cd0 dcgettext
0x407ce0 transcmp
0x407d60 plural_eval
0x408530 _nl_find_msg
0x409130 __dcigettext
0x409a30 _nl_find_domain
0x409cd0 _nl_load_domain
0x40b1d0 alias_compare
0x40b1f0 read_alias_file
0x40b6d0 _nl_expand_alias
0x40b8a0 _nl_make_l10nflist
0x40be70 _nl_normalize_codeset
0x40bf90 _nl_explode_name
0x40c1d0 __gettext_free_exp
0x40c4f0 new_exp.constprop.3
0x40fb60 new_exp
0x4132f0 __gettextparse
0x413b40 __gettext_extract_plural
0x413c40 __hash_string
0x413c80 sub_413c80
0x413c90 gsignal
0x413dc0 __libc_sigaction
0x413fa0 sigaction
0x413fd0 abort
0x414210 msort_with_tmp.part.0
0x414660 qsort_r
0x414ae0 qsort
0x414af0 getenv
0x414bd0 __run_exit_handlers
0x414e50 exit
0x414e70 __new_exitfn
0x414f90 __internal_atexit
0x415090 __cxa_atexit
0x415190 sub_415190
0x4151a0 strtoll
0x4151c0 sub_4151c0
0x4151d0 strtoull
0x4151f0 ____strtoll_l_internal
0x4156a0 strtol_l
0x4159b0 ____strtoull_l_internal
0x415dd0 strtoul_l
0x416040 __correctly_grouped_prefixmb
0x416260 snprintf
0x416310 __asprintf
0x4163d0 __isoc99_sscanf
0x416490 __isoc99_vsscanf
0x416540 locked_vfxprintf
0x4166b0 __fxprintf
0x416830 __fxprintf_nocancel
0x4169c0 _IO_fclose
0x416bfa sub_416bfa
0x416c50 fflush
0x416d5f sub_416d5f
0x416e10 __fopen_internal
0x416f20 fopen
0x417040 fread
0x417161 sub_417161
0x4171c0 puts
0x41736d sub_41736d
0x4173c0 adjust_wide_data
0x4174b0 _IO_wfile_underflow
0x417b30 _IO_wfile_seekoff
0x4183d0 _IO_wfile_underflow_maybe_mmap
0x418410 _IO_wfile_underflow_mmap
0x418580 _IO_wdo_write
0x418a20 _IO_wfile_sync
0x418bb0 _IO_wfile_xsputn
0x418eb0 ferror
0x418fa0 getc
0x4190b6 sub_4190b6
0x419110 putc
0x419230 sub_419230
0x419290 vasprintf
0x419420 _IO_strn_overflow
0x419480 __vsnprintf
0x419570 __libc_message.constprop.0
0x4196f0 __libc_message
0x4199e0 __libc_fatal
0x419a00 _IO_vtable_check
0x419a20 fgets_unlocked
0x419ad0 _IO_file_seekoff_maybe_mmap
0x419b50 sub_419b50
0x419b60 _IO_file_setbuf
0x419b90 _IO_file_setbuf_mmap
0x419c10 _IO_file_underflow
0x419e91 sub_419e91
0x419f20 sub_419f20
0x419f30 _IO_file_sync_mmap
0x419f90 _IO_file_xsgetn_maybe_mmap
0x41a1a0 _IO_file_seekoff
0x41a7a0 _IO_file_write
0x41a850 _IO_file_xsgetn_mmap
0x41aba0 _IO_file_xsgetn
0x41ae00 _IO_file_seekoff_mmap
0x41af20 _IO_file_read
0x41af40 _IO_file_xsputn
0x41b270 _IO_file_underflow_maybe_mmap
0x41b470 _IO_file_underflow_mmap
0x41b720 _IO_new_file_init_internal
0x41b750 _IO_file_init
0x41b780 _IO_file_open
0x41b860 _IO_file_attach
0x41b920 _IO_do_write
0x41baa0 _IO_file_close_it
0x41bc40 _IO_file_fopen
0x41c570 _IO_file_finish
0x41c610 _IO_file_overflow
0x41c820 _IO_file_sync
0x41c910 save_for_backup
0x41cae0 flush_cleanup
0x41cb90 _IO_cleanup
0x41d060 _IO_un_link
0x41d330 _IO_link_in
0x41d5d0 _IO_switch_to_main_get_area
0x41d600 _IO_switch_to_backup_area
0x41d630 _IO_switch_to_get_mode
0x41d6d0 _IO_free_backup_area
0x41d720 __overflow
0x41d790 __underflow
0x41d980 __uflow
0x41db90 _IO_setb
0x41dbf0 _IO_doallocbuf
0x41dca0 sub_41dca0
0x41dcb0 _IO_default_uflow
0x41dd10 _IO_default_xsputn
0x41de20 _IO_sgetn
0x41de90 _IO_default_xsgetn
0x41e110 _IO_default_setbuf
0x41e240 _IO_default_seekpos
0x41e2b0 _IO_default_doallocate
0x41e310 _IO_init_internal
0x41e3e0 _IO_init
0x41e4b0 _IO_enable_locks
0x41e4f0 _IO_old_init
0x41e5a0 _IO_no_init
0x41e6f0 sub_41e6f0
0x41e700 _IO_default_finish
0x41ea30 _IO_sputbackc
0x41eab0 _IO_sungetc
0x41eb30 _IO_adjust_column
0x41eb70 _IO_flush_all_lockp
0x41ee40 _IO_flush_all
0x41f0f0 _flushlbf
0x41f380 _IO_init_marker
0x41f450 _IO_remove_marker
0x41f490 sub_41f490
0x41f4a0 _IO_marker_delta
0x41f4d0 _IO_seekmark
0x41f570 _IO_unsave_markers
0x41f5e0 _IO_default_pbackfail
0x41f760 _IO_default_seekoff
0x41f770 sub_41f770
0x41f780 _IO_default_seek
0x41f790 sub_41f790
0x41f7a0 sub_41f7a0
0x41f7b0 sub_41f7b0
0x41f7c0 sub_41f7c0
0x41f7d0 sub_41f7d0
0x41f7e0 sub_41f7e0
0x41f7f0 sub_41f7f0
0x41f800 _IO_list_lock
0x41f860 unlock
0x41f8b0 cilkg_deinit_global_state
0x41f8d0 _IO_str_underflow
0x41f930 _IO_str_overflow
0x41fad0 enlarge_userbuf
0x41fcb0 _IO_str_seekoff
0x41ff60 _IO_wstr_pbackfail
0x41ff80 _IO_str_finish
0x41ffb0 _IO_str_init_static_internal
0x420050 _IO_str_init_static
0x4200f0 _IO_str_init_readonly
0x420170 _IO_str_count
0x420190 _dl_tunable_set_arena_max
0x4201a0 _dl_tunable_set_arena_test
0x4201b0 _dl_tunable_set_tcache_max
0x4201f0 _dl_tunable_set_tcache_count
0x420200 _dl_tunable_set_tcache_unsorted_limit
0x420210 int_mallinfo
0x420300 _dl_tunable_set_trim_threshold
0x420320 _dl_tunable_set_top_pad
0x420340 _dl_tunable_set_mmap_threshold
0x420360 _dl_tunable_set_mmaps_max
0x420380 sub_420380
0x420390 malloc_printerr
0x4203b0 malloc_consolidate
0x420650 new_heap
0x420800 _dl_tunable_set_mallopt_check
0x420870 __malloc_info.part.10
0x420db0 gomp_iter_guided_next
0x420e70 ptmalloc_init.part.0
0x4210e0 arena_get2.part.3
0x4217a0 get_free_list
0x4219b0 arena_get_retry
0x421a90 munmap_chunk
0x421b60 mremap_chunk
0x421d50 free_check
0x4225e0 _int_free
0x4232f0 sysmalloc
0x423c10 _int_malloc
0x424c20 malloc_check
0x424dd0 _int_memalign
0x425020 _int_realloc
0x425490 realloc_check
0x425d80 tcache_init.part.4
0x425ec0 memalign_check
0x426350 malloc_hook_ini
0x426950 __malloc
0x426ce0 memalign_hook_ini
0x427210 __free
0x427fe0 realloc_hook_ini
0x428410 sub_428410
0x428d09 sub_428d09
0x428ff0 sub_428ff0
0x429010 sub_429010
0x429050 sub_429050
0x429200 __pvalloc
0x429760 __calloc
0x429bb0 malloc_trim
0x429ec0 sub_429ec0
0x42a0a0 malloc_stats
0x42a2b0 __mallopt
0x42a4a0 posix_memalign
0x42a860 malloc_info
0x42a8b0 __default_morecore
0x42a8d0 index
0x42a910 strcmp
0x42a940 __atomic_test_and_set_16
0x42a970 __atomic_exchange_16
0x42a990 strdup
0x42a9e0 strlen
0x42aa10 strncmp
0x42aa50 __atomic_fetch_and_16
0x42b530 strstr
0x42b550 __memchr
0x42b580 wmemcmp
0x42b5e0 memmove
0x42b6a0 memset
0x42b740 mempcpy
0x42b800 __atomic_and_fetch_16
0x42b830 __atomic_store_16
0x42b860 strcasecmp_l
0x42b8b0 memcpy
0x42b970 rawmemchr
0x42b9a0 strchrnul
0x42b9d0 __stpncpy_sse2
0x42ba30 __strncpy_sse2
0x42ba80 __strcmp_ssse3
0x42e3d0 __strncmp_sse2
0x42fc20 __strncmp_ssse3
0x431380 __strncmp_sse42
0x432890 __memchr_avx2
0x432b60 __rawmemchr_avx2
0x432ca0 __memcmp_sse2
0x4330a0 __memcmp_avx2_movbe
0x433480 __memcmp_sse4_1
0x438b7b GOMP_cancellation_point.part.3
0x43cc40 sub_43cc40
0x443050 sub_443050
0x443250 sub_443250
0x443450 sub_443450
0x443650 sub_443650
0x443850 sub_443850
0x443a50 sub_443a50
0x443c50 sub_443c50
0x443e50 sub_443e50
0x444050 sub_444050
0x44411c sub_44411c
0x444120 sub_444120
0x444140 sub_444140
0x449d90 sub_449d90
0x449f10 sub_449f10
0x44a090 sub_44a090
0x44a210 sub_44a210
0x44a390 sub_44a390
0x44a510 sub_44a510
0x44a690 sub_44a690
0x44a810 sub_44a810
0x44a990 sub_44a990
0x44ab10 sub_44ab10
0x44ac90 sub_44ac90
0x44ae10 sub_44ae10
0x44af90 sub_44af90
0x44b110 sub_44b110
0x44b7b0 sub_44b7b0
0x44ba70 sub_44ba70
0x44bd40 sub_44bd40
0x44c3d0 __stpcpy_ssse3
0x44dbe0 __stpncpy_ssse3
0x450830 __strcpy_sse2_unaligned
0x451330 sub_451330
0x451360 sub_451360
0x451380 sub_451380
0x451850 sub_451850
0x451860 sub_451860
0x451870 sub_451870
0x451880 sub_451880
0x451890 sub_451890
0x4518a0 sub_4518a0
0x4518b0 sub_4518b0
0x4518c0 sub_4518c0
0x4518d0 sub_4518d0
0x4518e0 sub_4518e0
0x4518f0 sub_4518f0
0x451900 sub_451900
0x451910 sub_451910
0x451920 sub_451920
0x451930 sub_451930
0x451940 sub_451940
0x451950 sub_451950
0x451960 sub_451960
0x451970 sub_451970
0x451990 sub_451990
0x4519a0 sub_4519a0
0x4519b0 sub_4519b0
0x4519d0 sub_4519d0
0x4519f0 sub_4519f0
0x451a10 sub_451a10
0x451a30 sub_451a30
0x451a50 sub_451a50
0x451a70 sub_451a70
0x451a90 sub_451a90
0x451ab0 sub_451ab0
0x451ad0 sub_451ad0
0x451af0 sub_451af0
0x451b10 sub_451b10
0x451b30 sub_451b30
0x451b50 sub_451b50
0x451b60 sub_451b60
0x451b70 sub_451b70
0x451b80 sub_451b80
0x451b90 sub_451b90
0x451ba0 sub_451ba0
0x451bb0 sub_451bb0
0x451bc0 sub_451bc0
0x451bd0 sub_451bd0
0x451be0 sub_451be0
0x451bf0 sub_451bf0
0x451c00 sub_451c00
0x451c10 sub_451c10
0x451c20 sub_451c20
0x451c30 sub_451c30
0x451c40 sub_451c40
0x451c50 sub_451c50
0x451c60 sub_451c60
0x4529e0 sub_4529e0
0x452a10 sub_452a10
0x452a30 sub_452a30
0x453370 sub_453370
0x453380 sub_453380
0x453390 sub_453390
0x4533a0 sub_4533a0
0x4533b0 sub_4533b0
0x4533c0 sub_4533c0
0x4533d0 sub_4533d0
0x4533e0 sub_4533e0
0x4533f0 sub_4533f0
0x453400 sub_453400
0x453410 sub_453410
0x453420 sub_453420
0x453430 sub_453430
0x453440 sub_453440
0x453450 sub_453450
0x453460 sub_453460
0x453470 sub_453470
0x453480 sub_453480
0x455280 sub_455280
0x455540 sub_455540
0x455570 sub_455570
0x455590 __strcspn_sse2
0x455630 __strcspn_sse42
0x455770 sub_455770
0x4559f0 __mempcpy_sse2_unaligned
0x455a00 __memcpy_sse2_unaligned
0x455a30 sub_455a30
0x455a50 sub_455a50
0x455a90 __mempcpy_sse2_unaligned_erms
0x455aa0 __memmove_sse2_unaligned_erms
0x455da0 __mempcpy_avx_unaligned
0x455db0 __memcpy_avx_unaligned
0x455de0 __mempcpy_avx_unaligned_erms
0x455df0 __memmove_avx_unaligned_erms
0x4561d0 __mempcpy_avx512_unaligned
0x4561e0 __memcpy_avx512_unaligned
0x456220 __mempcpy_avx512_unaligned_erms
0x456230 __memmove_avx512_unaligned_erms
0x456730 bzero
0x456760 __memset_sse2_unaligned
0x456790 sub_456790
0x4568a0 __wmemset_avx2_unaligned
0x4568c0 __memset_avx2_unaligned
0x4568f0 __memset_avx2_erms
0x456a20 __wmemset_avx512_unaligned
0x456a40 __memset_avx512_unaligned
0x456a80 __memset_avx512_erms
0x456c00 handle_amd
0x456d3d sub_456d3d
0x456d44 sub_456d44
0x456d4b sub_456d4b
0x456d52 sub_456d52
0x456d59 sub_456d59
0x456d60 sub_456d60
0x456d67 sub_456d67
0x456d6e sub_456d6e
0x456d8a sub_456d8a
0x456dc0 intel_check_word.isra.0
0x4570c0 handle_intel.constprop.1
0x457220 __cache_sysconf
0x457290 wmempcpy
0x4572a0 mbsrtowcs
0x4572c0 _nl_cleanup_ctype
0x457310 __wcsmbs_getfct
0x457390 __wcsmbs_load_conv
0x457660 __wcsmbs_clone_conv
0x4576e0 __wcsmbs_named_conv
0x4577e0 __mbsrtowcs_l
0x457b60 _Exit
0x457b80 sub_457b80
0x457b8f sub_457b8f
0x457bc0 __sysconf_check_spec
0x457cd0 sysconf
0x4580b0 sched_yield
0x4580e0 __get_child_max
0x458130 _xstat
0x458180 _fxstat
0x4581d0 __open64
0x4582f0 __open_nocancel
0x458390 __read
0x458430 __read_nocancel
0x458460 __write
0x458500 __write_nocancel
0x458530 lseek
0x458560 __fcntl
0x458680 __fcntl_nocancel
0x458730 __libc_close
0x4587b0 __close_nocancel
0x4587e0 getcwd
0x458f00 __GI_getrlimit
0x458f40 sbrk
0x458fd0 getpagesize
0x459010 getdtablesize
0x459060 mmap64
0x459140 munmap
0x459170 mprotect
0x4591a0 madvise
0x4591d0 trecurse
0x459260 tdestroy_recurse
0x459320 tsearch
0x459700 tfind
0x459760 tdelete
0x459d10 twalk
0x459dc0 tdestroy
0x459f80 next_line
0x45a130 get_nprocs
0x45a5c0 get_nprocs_conf
0x45a6a0 get_phys_pages
0x45a730 get_avphys_pages
0x45a7c0 __getclktck
0x45a7e0 __init_misc
0x45a840 mremap
0x45a870 sysinfo
0x45a8a0 __libc_alloca_cutoff
0x45a8e0 __lll_lock_wait_private
0x45a910 __lll_unlock_wake_private
0x45a930 __libc_enable_asynccancel
0x45a990 __libc_disable_asynccancel
0x45a9f0 __fprintf_chk
0x45abc0 __chk_fail
0x45abd0 __explicit_bzero_chk_internal
0x45ac00 __stack_chk_fail_local
0x45ac20 __fortify_fail_abort
0x45ac90 __fortify_fail
0x45acb0 _dl_debug_state
0x45acc0 _dl_debug_initialize
0x45ad40 __tunable_set_val
0x45adc0 __tunables_init
0x45b3c0 __tunable_get_val
0x45b420 _dl_aux_init
0x45b830 _dl_non_dynamic_init
0x45c130 __libc_init_secure
0x45c180 _dl_mcount_wrapper
0x45c190 _dl_mcount_wrapper_check
0x45c1c0 _dl_tunable_set_hwcaps
0x45cd60 _dl_discover_osversion
0x45ce70 __libc_init_first
0x45cf00 sub_45cf00
0x45cf10 __gconv_open
0x45d420 __gconv
0x45d630 __gconv_close
0x45d690 sub_45d690
0x45d6a0 derivation_compare
0x45d6e0 find_derivation
0x45e240 __gconv_release_step
0x45e2a0 __gconv_compare_alias
0x45e3b0 __gconv_find_transform
0x45e6c0 __gconv_close_transform
0x45e7d0 insert_module
0x45e8d0 add_module.isra.0
0x45ec60 __gconv_get_path
0x45f050 __gconv_read_conf
0x45f630 __gconv_get_builtin_trans
0x45f890 __atomic_fetch_add_1
0x45f8a0 __gconv_transform_internal_ucs4
0x45fd30 __gconv_transform_ucs4_internal
0x460360 __gconv_transform_internal_ucs4le
0x4607f0 __gconv_transform_ucs4le_internal
0x460e40 __gconv_transform_ascii_internal
0x461250 __gconv_transform_internal_ascii
0x461c30 __gconv_transform_internal_utf8
0x462c50 __gconv_transform_utf8_internal
0x463dc0 __gconv_transform_ucs2_internal
0x464550 __gconv_transform_internal_ucs2
0x464fa0 __gconv_transform_ucs2reverse_internal
0x465790 __gconv_transform_internal_ucs2reverse
0x466200 __gconv_transliterate
0x466730 __gconv_load_cache
0x466940 __gconv_compare_alias_cache
0x466af0 __gconv_lookup_cache
0x467430 _ZN11__sanitizer18InternalSymbolizer5FlushEv
0x467450 sub_467450
0x467460 do_release_shlib
0x4674e0 __gconv_find_shlib
0x4676c0 __gconv_release_shlib
0x4676e0 new_composite_name
0x4679a0 setlocale
0x468280 _nl_find_locale
0x468aa0 _nl_intern_locale_data
0x468ce0 _nl_load_locale
0x4692b0 _nl_unload_locale
0x469310 _nl_load_locale_from_archive
0x469830 _nl_postload_ctype
0x4698b0 __current_locale_name
0x4698d0 _ZN11__sanitizer8DTLS_GetEv
0x4698f0 __ctype_b_loc
0x469910 __ctype_toupper_loc
0x469930 __ctype_init
0x469980 __setfpucw
0x4699d0 __sigsetjmp
0x469a30 __sigjmp_save
0x469a60 sigprocmask
0x469aa0 _quicksort
0x46af20 __add_to_environ
0x46b2a0 setenv
0x46b300 unsetenv
0x46b440 clearenv
0x46b500 secure_getenv
0x46b520 group_number
0x46b650 _i18n_number_rewrite#2
0x46b8e0 _IO_helper_overflow
0x46b9c0 printf_positional
0x46def0 vfprintf
0x471010 buffered_vfprintf
0x471270 hack_digit
0x4713b0 _i18n_number_rewrite#3
0x471640 __printf_fp_l
0x474140 __printf_fp
0x474160 __guess_grouping
0x4741b0 sub_4741b0
0x4742c0 sub_4742c0
0x4743d0 __printf_fphex
0x476700 register_printf_modifier
0x4768c0 __handle_registered_modifier_mb
0x4769a0 __handle_registered_modifier_wc
0x476a70 register_printf_type
0x476b60 fprintf
0x476c20 _i18n_number_rewrite
0x476db0 _IO_helper_overflow#2
0x476ec0 sub_476ec0
0x479760 sub_479760
0x47c980 buffered_vfprintf#2
0x47cbe0 char_buffer_add_slow
0x47cc50 _IO_vfscanf
0x484e30 sub_484e30
0x484e40 _IO_funlockfile
0x484e90 __parse_one_specmb
0x485620 __parse_one_specwc
0x485ed0 _IO_file_doallocate
0x486020 fputs
0x48615a sub_48615a
0x486230 fwrite
0x4863cd sub_4863cd
0x486430 __getdelim
0x486707 sub_486707
0x486760 _IO_getline
0x4868c0 _IO_getline_info
0x486a40 _IO_padn
0x486b80 _IO_wpadn
0x486cc0 save_for_wbackup.isra.0
0x486f40 _ZN11__sanitizer14ThreadRegistry13QuarantinePopEv
0x486f80 _IO_switch_to_main_wget_area
0x486fc0 _IO_switch_to_wbackup_area
0x487000 _IO_wsetb
0x487070 _IO_wdefault_pbackfail
0x487230 _IO_wdefault_finish
0x4872b0 _IO_wdefault_uflow
0x487320 __woverflow
0x4873a0 __wuflow
0x4875a0 __wunderflow
0x487790 _IO_wdefault_xsputn
0x487a40 _IO_wdefault_xsgetn
0x487e80 _IO_wdoallocbuf
0x487f20 _IO_wdefault_doallocate
0x487f90 _IO_switch_to_wget_mode
0x488010 _IO_free_wbackup_area
0x488080 _IO_sputbackwc
0x488100 _IO_sungetwc
0x488180 _IO_adjust_wcolumn
0x4881e0 _IO_init_wmarker
0x4882b0 goacc_restore_bind
0x488300 _IO_seekwmark
0x4883b0 _IO_unsave_wmarkers
0x488440 do_encoding
0x488460 sub_488460
0x488470 do_max_length
0x488480 do_in
0x488570 do_unshift
0x488650 do_out
0x488750 do_length
0x488810 _IO_fwide
0x488a10 __libc_scratch_buffer_grow_preserve
0x488ac0 __libc_scratch_buffer_set_array_size
0x488b80 strndup
0x488bd0 strerror_r
0x488dd0 strtok_r
0x488e40 two_way_long_needle
0x489250 memmem
0x489610 argz_create_sep
0x4896f0 argz_add_sep
0x4897b0 __strrchr_sse2
0x489aa0 __strrchr_avx2
0x489c70 __strnlen_sse2
0x489e90 __strnlen_avx2
0x48a1b0 wmemchr
0x48a1e0 sub_48a1e0
0x48a1f0 wmemmove
0x48a200 wmemset
0x48a240 btowc
0x48a400 mbrlen
0x48a420 mbrtowc
0x48a640 wcrtomb
0x48a820 wcsrtombs
0x48ab50 wcschrnul
0x48ab70 __wcsnlen_sse4_1
0x48ad90 __wcsnlen_sse2
0x48ae30 __wcslen_sse2
0x48b0d0 __wcslen_avx2
0x48b280 __wcsnlen_avx2
0x48b5d0 time
0x48b5e0 __opendirat
0x48b760 opendir
0x48b8e0 __alloc_dir
0x48b9f0 closedir
0x48ba20 readdir
0x48bb20 rewinddir
0x48bbb0 __getdents64
0x48bc40 fdopendir
0x48bd00 uname
0x48bd30 getuid
0x48bd40 geteuid
0x48bd50 getgid
0x48bd60 getegid
0x48bd70 _lxstat
0x48bdc0 __GI___fxstatat64
0x48be20 __openat64
0x48bf40 __openat_nocancel
0x48bfe0 isatty
0x48c020 tcgetattr
0x48c0e0 brk
0x48c140 wctrans
0x48c1d0 towctrans
0x48c210 __readonly_area
0x48c400 is_trusted_path_normalize
0x48c640 sub_48c640
0x48c6c0 open_verify.constprop.7
0x48cc50 open_path
0x48d290 _dl_map_object_from_fd.constprop.8
0x48e400 _dl_dst_count
0x48e6b0 _dl_dst_substitute
0x48ea30 expand_dynamic_string_token
0x48eb50 sub_48eb50
0x48ef30 cache_rpath.part.6
0x48f150 _dl_init_paths#2
0x48f430 _dl_map_object
0x48fe70 _dl_rtld_di_serinfo
0x4904a0 do_lookup_x
0x491310 _dl_lookup_symbol_x
0x491dd0 _dl_setup_hash
0x491e80 _dl_add_to_namespace_list
0x491f40 _dl_new_object
0x492250 _ZN11__sanitizer15POSIXSymbolizer21CanReturnFileLineInfoEv
0x492310 sub_492310
0x4923c0 _dl_nothread_init_static_tls
0x492400 sub_492400
0x492470 _dl_reloc_bad_type
0x492540 _dl_relocate_object
0x493df0 _dl_important_hwcaps
0x4945c0 _dl_debug_vdprintf
0x494b70 _dl_sysdep_read_whole_file
0x494c00 sub_494c00
0x494cb0 sub_494cb0
0x494d60 _dl_dprintf
0x494e00 _dl_name_match_p
0x494e70 _dl_higher_prime_number
0x494ef0 _dl_strtoul
0x495050 _dl_start_profile
0x495800 _dl_mcount
0x495a60 _dl_next_tls_modid
0x495bf0 _dl_allocate_tls_storage
0x495cc0 _dl_allocate_tls_init
0x495fe0 _dl_allocate_tls
0x496050 _dl_deallocate_tls
0x4960d0 _dl_tls_get_addr_soft
0x496150 _dl_add_to_slotinfo
0x496240 _dl_get_origin
0x4963e0 _dl_scope_free
0x4964b0 _dl_make_stack_executable
0x496510 _dl_runtime_profile_avx512
0x496990 _dl_runtime_profile_avx
0x496e10 _dl_runtime_profile_sse
0x497010 _dl_runtime_resolve_fxsave
0x497090 _dl_runtime_resolve_xsave
0x497160 _dl_runtime_resolve_xsavec
0x497220 sub_497220
0x497250 _dl_exception_create
0x497330 _dl_exception_create_format
0x497610 _dl_exception_free
0x497640 _dl_cache_libcmp
0x497730 _dl_load_cache_lookup
0x498260 _dl_unload_cache
0x4982a0 sub_4982a0
0x4982b0 _dl_tlsdesc_undefweak
0x4982c0 _dl_tlsdesc_resolve_rela
0x498330 _dl_tlsdesc_resolve_hold
0x4983b0 do_dlopen
0x4983f0 do_dlsym_private
0x498480 do_dlsym
0x4984c0 do_dlvsym
0x498500 sub_498500
0x498510 __libc_dlclose
0x4985a0 __libc_dlsym
0x498660 __libc_dlvsym
0x4987d0 __libc_dlopen_mode
0x4989d0 __libc_dlsym_private
0x498a90 __libc_register_dl_open_hook
0x498bf0 fatal_error
0x498cc0 _dl_signal_exception
0x498d10 _dl_signal_error
0x498d60 _dl_catch_exception
0x498e30 _dl_catch_error
0x498ea0 __longjmp
0x498f00 sub_498f00
0x498f10 sub_498f10
0x498f30 sub_498f30
0x498f40 sub_498f40
0x498f60 sub_498f60
0x498f70 sub_498f70
0x498f90 str_to_mpn.isra.0
0x499290 round_and_return#2
0x499810 ____strtof_l_internal
0x49c0d0 strtof32_l
0x49c0e0 str_to_mpn.isra.0#2
0x49c3e0 round_and_return
0x49c980 ____strtod_l_internal
0x49eed0 str_to_mpn.isra.0#3
0x49f1f0 round_and_return#3
0x49f710 ____strtold_l_internal
0x4a1ba0 __strtof_nan
0x4a1c50 __strtod_nan
0x4a1d30 __strtold_nan
0x4a1e00 __mpn_sub_n
0x4a1eb0 __mpn_cmp
0x4a1ef0 __mpn_divrem
0x4a24b0 __mpn_lshift
0x4a25c0 __mpn_rshift
0x4a26d0 __mpn_mul
0x4a2b00 __mpn_mul_1
0x4a2c20 __mpn_impn_mul_n_basecase
0x4a2de0 __mpn_impn_mul_n
0x4a3350 __mpn_impn_sqr_n_basecase
0x4a3500 __mpn_impn_sqr_n
0x4a39f0 __mpn_mul_n
0x4a3a90 __mpn_add_n
0x4a3b40 __mpn_submul_1
0x4a3c30 __mpn_extract_double
0x4a3cc0 __mpn_extract_long_double
0x4a3d80 __mpn_construct_float
0x4a3db0 __mpn_construct_double
0x4a3df0 __mpn_construct_long_double
0x4a3e40 __mpn_extract_float128
0x4a3f60 _itoa_word
0x4a4030 _fitoa_word
0x4a41e0 __dlerror
0x4a4470 _dlerror_run
0x4a45e0 __libc_register_dlfcn_hook
0x4a4610 __register_frame_info_table#2
0x4a4620 __dladdr1
0x4a4650 sub_4a4650
0x4a4740 __dlinfo
0x4a47a0 sub_4a47a0
0x4a4810 __dlmopen
0x4a4890 strerror
0x4a4920 strspn
0x4a4940 strncasecmp_l
0x4a4990 strsep
0x4a49e0 sub_4a49e0
0x4ab0c0 sub_4ab0c0
0x4ab540 sub_4ab540
0x4ab680 fchflags
0x4ab920 sub_4ab920
0x4acef0 sub_4acef0
0x4acf10 __strpbrk_sse2
0x4acfb0 __strspn_sse42
0x4ad120 getpid
0x4ad130 __profil_counter
0x4ad180 profil
0x4ad320 __profile_frequency
0x4ad330 _dl_fixup
0x4ad4d0 _dl_profile_fixup
0x4ad6f0 sub_4ad6f0
0x4ad700 add_to_global
0x4ad990 _dl_find_dso_for_object
0x4ada20 _dl_open
0x4adc30 _dl_show_scope
0x4add60 dl_open_worker
0x4ae580 remove_slotinfo
0x4ae6d0 _dl_close_worker.part.0
0x4af520 _dl_close_worker
0x4af5a0 sub_4af5a0
0x4af5fa sub_4af5fa
0x4af620 sub_4af620
0x4af6a0 _dl_sort_maps
0x4af990 _dl_tlsdesc_resolve_rela_fixup
0x4afb30 _dl_tlsdesc_resolve_hold_fixup
0x4afba0 _dl_unmap
0x4afbc0 _dl_addr
0x4afec0 _dl_addr_inside_object
0x4aff20 __mpn_addmul_1
0x4b0010 sub_4b0010
0x4b0090 __dlopen
0x4b0120 __dlclose
0x4b0150 dlsym_doit
0x4b0170 __dlsym
0x4b0220 dlvsym_doit
0x4b0240 __dlvsym
0x4b0300 setitimer
0x4b0330 openaux
0x4b0370 _dl_build_local_scope
0x4b0460 _dl_map_object_deps
0x4b16f0 _dl_init
0x4b1a60 _dl_check_map_versions
0x4b2100 _dl_check_all_versions
0x4b2170 call_dl_lookup
0x4b21a0 _dl_vsym
0x4b24a0 _dl_sym
0x4b26d0 __unordtf2
0x4b28a0 __lttf2
0x4b2ac0 __sfp_handle_exceptions
0x4b2b50 read_encoded_value_with_base#2
0x4b2c90 base_of_encoded_value#2
0x4b2d00 execute_cfa_program
0x4b3670 init_dwarf_reg_size_table
0x4b36f0 uw_frame_state_for
0x4b3d80 execute_stack_op
0x4b4540 uw_update_context_1
0x4b4970 uw_init_context_1
0x4b4af0 uw_update_context
0x4b4b80 _Unwind_RaiseException_Phase2
0x4b4c30 _Unwind_ForcedUnwind_Phase2
0x4b4d00 uw_install_context_1
0x4b4ec0 _Unwind_GetGR
0x4b4f20 _Unwind_SetGR
0x4b4f60 _Unwind_GetIP
0x4b4f70 _Unwind_GetIPInfo
0x4b4f90 _Unwind_SetIP
0x4b4fa0 _Unwind_GetLanguageSpecificData
0x4b4fb0 _Unwind_GetRegionStart
0x4b4fc0 _Unwind_FindEnclosingFunction
0x4b4ff0 _Unwind_GetDataRelBase
0x4b5000 _Unwind_GetTextRelBase
0x4b5010 __frame_state_for
0x4b5120 sub_4b5120
0x4b5130 _Unwind_RaiseException
0x4b5440 _Unwind_ForcedUnwind
0x4b55e0 _Unwind_Resume
0x4b5770 _Unwind_Resume_or_Rethrow
0x4b5920 _Unwind_DeleteException
0x4b5940 _Unwind_Backtrace
0x4b59d0 fde_unencoded_compare
0x4b59f0 frame_downheap
0x4b5ac0 frame_heapsort
0x4b5b70 read_encoded_value_with_base#3
0x4b5cb0 get_cie_encoding
0x4b5df0 size_of_encoded_value.part.3
0x4b5e40 base_from_object.part.4
0x4b5e90 fde_single_encoding_compare
0x4b5f20 linear_search_fdes
0x4b6120 fde_mixed_encoding_compare
0x4b61d0 classify_object_over_fdes
0x4b6350 add_fdes
0x4b6530 search_object
0x4b6ca0 base_from_cb_data.part.5
0x4b6cf0 _Unwind_IteratePhdrCallback
0x4b71a0 __register_frame_info_bases.part.6
0x4b7240 __register_frame_info_bases
0x4b7260 __register_frame_info
0x4b7290 __register_frame_table#2
0x4b72b0 sub_4b72b0
0x4b7320 _dl_get_tls_static_info
0x4b7350 __register_frame_info_table
0x4b7360 __register_frame_table
0x4b7380 __deregister_frame_info_bases
0x4b74a0 sub_4b74a0
0x4b74b0 __deregister_frame
0x4b74e0 _Unwind_Find_FDE
0x4b7700 base_of_encoded_value
0x4b7770 read_encoded_value_with_base
0x4b78b0 __gcc_personality_v0
0x4b7b30 dl_iterate_phdr
0x4b7c50 free_mem#4
0x4b7d10 _nl_finddomain_subfreeres
0x4b7d60 _nl_unload_domain
0x4b7e60 buffer_free
0x4b7ea0 free_derivation
0x4b7f60 free_modules_db
0x4b8070 free_mem#8
0x4b8310 free_mem#3
0x4b8340 free_mem#2
0x4b8380 do_release_all
0x4b83a0 free_mem#5
0x4b83d0 sub_4b83d0
0x4b8b90 free_mem#6
0x4b8c70 free_mem
0x4b8cd0 free_slotinfo
0x4b8db0 free_mem#7
0x4b9180 arena_thread_freeres
0x4ba210 _fini
"""
import idaapi
import idautils
import idc
for l in shit.split('\n'):
    if not l: continue
    fuckers = l.split(' ')
    fuck = int(fuckers[0],16)
    shit = fuckers[1]
    if shit.startswith('sub_'): continue
    print(fuck,shit)
    eaaddr = fuck
    idc.MakeCode(eaaddr)
    idc.MakeFunction(eaaddr)
    idc.MakeNameEx(fuck, shit, idc.SN_NOWARN)
