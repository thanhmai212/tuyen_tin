import timeit
import random
import sys
import textwrap
from memory_profiler import memory_usage


def performance_arena():
    """
    Một công cụ dòng lệnh để người dùng nhập và so sánh TỐC ĐỘ và BỘ NHỚ
    của các đoạn mã Python.
    """
    print("--- 🏆 ĐẤU TRƯỜNG HIỆU NĂNG TOÀN DIỆN 🏆 ---")
    print("Các đấu sĩ sẽ được đánh giá trên cả TỐC ĐỘ và MỨC SỬ DỤNG BỘ NHỚ.")
    print("\nQUY TẮC:")
    print("1. Dữ liệu thử nghiệm đã được tạo sẵn trong các biến:")
    print("   - `a`: Một danh sách (list) chứa rất nhiều số nguyên.")
    print("   - `k_queries`: Một danh sách chứa các truy vấn.")
    print("2. Mã của bạn phải tính toán và trả về (return) kết quả.")
    print("   (Ví dụ: `ans = []`, `ans.append(...)`, cuối cùng là `return ans`)")
    print("3. Nhập code của bạn. Để kết thúc, hãy nhập một dòng trống.")
    print("4. Sau khi nhập xong tất cả các đoạn mã, gõ 'run' và Enter để bắt đầu.")
    print("-" * 60)

    # --- Thu thập các đoạn mã từ người dùng ---
    code_snippets = []
    snippet_count = 1
    while True:
        print(f"Nhập vào Đấu sĩ #{snippet_count} (hoặc gõ 'run' để bắt đầu):")

        lines = []
        try:
            while True:
                line = input()
                if not line: break
                lines.append(line)
        except EOFError:
            break

        code_block = "\n".join(lines)

        if lines and lines[0].strip().lower() == 'run':
            if not code_snippets:
                print("Chưa có đấu sĩ nào tham gia! Thoát chương trình.")
                return
            break

        if code_block:
            code_snippets.append(textwrap.dedent(code_block))
            snippet_count += 1
        elif not code_snippets:
            print("Snippet rỗng, vui lòng nhập lại.")
        else:
            print("Đã nhận đủ các đấu sĩ, bắt đầu so tài...")
            break

    # --- Chuẩn bị dữ liệu và cài đặt ---
    print("\n" + "=" * 22 + " CHUẨN BỊ ĐẤU TRƯỜNG " + "=" * 22)
    N_ELEMENTS = 50000
    Q_QUERIES = 10000
    MAX_VALUE = 1000
    NUM_TIME_EXECUTIONS = 3

    print(f"Kích thước dữ liệu: N = {N_ELEMENTS}, Q = {Q_QUERIES}")
    print("Đang tạo dữ liệu thử nghiệm ngẫu nhiên...")
    sys.stdout.flush()

    a = [random.randint(1, MAX_VALUE) for _ in range(N_ELEMENTS)]
    k_queries = [random.randint(1, N_ELEMENTS) for _ in range(Q_QUERIES)]

    print("-> Sẵn sàng!")
    print("\n" + "=" * 25 + " BẮT ĐẦU SO TÀI " + "=" * 26)

    # --- Đo lường từng đoạn mã ---
    benchmark_results = []
    for i, user_code in enumerate(code_snippets):
        print(f"\n⚡ Đang đánh giá Đấu sĩ #{i + 1}...")
        sys.stdout.flush()

        # Gói code của người dùng vào một hàm để đo lường
        func_name = f"user_func_{i}"
        full_code = f"def {func_name}():\n"
        full_code += textwrap.indent(user_code, '    ')

        avg_time = float('inf')
        peak_mem = float('inf')

        try:
            # Thực thi để định nghĩa hàm trong môi trường hiện tại
            exec(full_code, globals())

            # --- Đo lường bộ nhớ ---
            # memory_usage trả về mức sử dụng RAM (theo MiB) trong quá trình chạy hàm
            # Nó trả về một list, chúng ta lấy giá trị đỉnh (max)
            mem_usage_samples = memory_usage((globals()[func_name],), interval=0.01)
            peak_mem = max(mem_usage_samples)

            # --- Đo lường thời gian ---
            # Lưu ý: Chúng ta đo thời gian của hàm đã được gói
            stmt_to_time = f"{func_name}()"
            setup_to_time = f"from __main__ import {func_name}"

            total_time = timeit.timeit(
                stmt=stmt_to_time,
                setup=setup_to_time,
                globals=globals(),
                number=NUM_TIME_EXECUTIONS
            )
            avg_time = total_time / NUM_TIME_EXECUTIONS

            benchmark_results.append({'id': i, 'time': avg_time, 'mem': peak_mem})
            print(f"-> Hoàn thành!")
            print(f"   - Thời gian trung bình: {avg_time:.6f} giây")
            print(f"   - Bộ nhớ đỉnh        : {peak_mem:.4f} MiB")

        except Exception as e:
            print(f"-> LỖI! Đấu sĩ #{i + 1} đã bị loại do lỗi: {e}")
            benchmark_results.append({'id': i, 'time': float('inf'), 'mem': float('inf')})

    # --- Công bố kết quả ---
    print("\n" + "=" * 27 + " KẾT QUẢ " + "=" * 28)

    if not benchmark_results: return

    # Xếp hạng theo thời gian
    print("\n--- 🏁 Bảng xếp hạng TỐC ĐỘ (nhanh nhất trước) 🏁 ---")
    benchmark_results.sort(key=lambda x: x['time'])
    for rank, res in enumerate(benchmark_results):
        rank_str = f"Hạng {rank + 1}:"
        snippet_id = res['id'] + 1
        if res['time'] == float('inf'):
            result_str = "BỊ LOẠI DO LỖI"
        else:
            result_str = f"Thời gian: {res['time']:.6f} giây"
        print(f"{rank_str:<10} Đấu sĩ #{snippet_id} -> {result_str}")

    winner_time = benchmark_results[0]
    if winner_time['time'] != float('inf'):
        print(f"🏆 Người chiến thắng về TỐC ĐỘ là Đấu sĩ #{winner_time['id'] + 1}!")

    # Xếp hạng theo bộ nhớ
    print("\n--- 🧠 Bảng xếp hạng BỘ NHỚ (tiết kiệm nhất trước) 🧠 ---")
    benchmark_results.sort(key=lambda x: x['mem'])
    for rank, res in enumerate(benchmark_results):
        rank_str = f"Hạng {rank + 1}:"
        snippet_id = res['id'] + 1
        if res['mem'] == float('inf'):
            result_str = "BỊ LOẠI DO LỖI"
        else:
            result_str = f"Bộ nhớ đỉnh: {res['mem']:.4f} MiB"
        print(f"{rank_str:<10} Đấu sĩ #{snippet_id} -> {result_str}")

    winner_mem = benchmark_results[0]
    if winner_mem['mem'] != float('inf'):
        print(f"🏆 Người chiến thắng về BỘ NHỚ là Đấu sĩ #{winner_mem['id'] + 1}!")


if __name__ == "__main__":
    performance_arena()