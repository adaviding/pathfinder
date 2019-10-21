if __name__ == "__main__":
    import os
    os.makedirs("/tmp/lib_attacher_test/a/b/c/d/e/f", exist_ok=True)
    os.makedirs("/tmp/lib_attacher_test/a/b/c/w/x", exist_ok=True)
    os.makedirs("/tmp/lib_attacher_test/a/b/w/x/y/z", exist_ok=True)

    start_folder="/tmp/lib_attacher_test/a/b/c/d/e/f"
    target_sub_path = "w/x"
    extra_sub_path = "y/z"

    num_test_failures = 0

    import lib_attacher

    folder = lib_attacher.search_folder_hierarchy(
        start_folder=start_folder,
        target_sub_path=target_sub_path,
        extra_sub_path=extra_sub_path)

    if folder:
        folder = folder.replace("\\", "/")

    if folder == "/tmp/lib_attacher_test/a/b/w/x":
        print(f"SUCCESS:  Test 1 returned {folder}")
    else:
        print(f"FAILURE:  Test 1 returned {folder}")
        num_test_failures += 1

    folder = lib_attacher.search_folder_hierarchy(
        start_folder=start_folder,
        target_sub_path=target_sub_path,
        extra_sub_path=None)

    if folder:
        folder = folder.replace("\\", "/")

    if folder == "/tmp/lib_attacher_test/a/b/c/w/x":
        print(f"SUCCESS:  Test 2 returned {folder}")
    else:
        print(f"FAILURE:  Test 2 returned {folder}")
        num_test_failures += 1

    import shutil
    shutil.rmtree("/tmp/lib_attacher_test", ignore_errors=True)

    print("-----------------------")
    if num_test_failures == 0:
        print("SUCCESS:  All tests succeeded")
    else:
        print(f"FAILURE:  {num_test_failures} tests failed")