import streamlit as pd
import streamlit as st
import os

# Cấu hình trang ứng dụng
st.set_page_config(
    page_title="Vietcombank - Kịch bản Hướng dẫn Mở Thẻ",
    page_icon="🏦",
    layout="wide"
)

# Thêm CSS để giao diện mang màu sắc nhận diện thương hiệu Vietcombank (Xanh lá)
st.markdown("""
    <style>
    .main-title { color: #008A4B; font-size: 32px; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .step-title { color: #008A4B; font-size: 24px; font-weight: bold; }
    .section-box { padding: 15px; border-radius: 8px; background-color: #f8f9fa; border-left: 5px solid #008A4B; margin-bottom: 15px; }
    .voice-over { font-style: italic; color: #333333; }
    .action-text { color: #d9534f; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">HỆ THỐNG MÔ PHỎNG KỊCH BẢN VIDEO VCB</div>', unsafe_allow_html=True)

# Định nghĩa dữ liệu kịch bản từng bước
script_data = [
    {
        "title": "MỞ ĐẦU",
        "image_desc": "Nhân viên Vietcombank mỉm cười trước máy tính.",
        "image_file": "assets/intro.png",
        "voice": "Xin chào Quý khách! Chỉ vài bước đơn giản dưới đây, Quý khách có thể đăng ký mở thẻ online ngay tại nhà. Hãy làm theo hướng dẫn nhé!",
        "screen_text": "HƯỚNG DẪN ĐĂNG KÝ MỞ THẺ TRỰC TUYẾN",
        "actions": []
    },
    {
        "title": "Bước 1: Truy cập vào website",
        "image_desc": "Quay màn hình gõ địa chỉ vietcombank.com.vn, sau đó chuyển sang gõ dangkydichvu.vietcombank.com.vn",
        "image_file": "assets/step1.png",
        "voice": "Quý khách có 2 cách: Cách 1: vào https://www.vietcombank.com.vn/vi-VN, tại mục Khách hàng cá nhân, bấm Đăng ký dịch vụ. Cách 2: truy cập trực tiếp vào https://dangkydichvu.vietcombank.com.vn/ để vào đăng ký dịch vụ luôn",
        "screen_text": "Website Vietcombank / Trang Đăng ký dịch vụ",
        "actions": [
            "Con trỏ di vào mục 'Khách hàng cá nhân' → di xuống 'Đăng ký dịch vụ' (click).",
            "Mở tab mới, gõ link dangkydichvu... và Enter."
        ]
    },
    {
        "title": "Bước 2: CHỌN TÍNH NĂNG ĐĂNG KÝ",
        "image_desc": "Giao diện trang đăng ký dịch vụ hiển thị. Có nút 'Đăng ký trực tuyến' ở giữa, và các nút 'Đăng ký' nhỏ ở từng sản phẩm.",
        "image_file": "assets/step2.png",
        "voice": "Tại đây, Quý khách chọn tính năng Đăng ký trực tuyến trên màn hình chính. Hoặc có thể chọn mục Đăng ký tại sản phẩm dịch vụ tương ứng.",
        "screen_text": "Nút 'Đăng ký trực tuyến' nổi bật ở giữa",
        "actions": ["Con trỏ click vào nút to 'Đăng ký trực tuyến' ở giữa màn hình (hoặc click vào nút Đăng ký của một sản phẩm bất kỳ)."]
    },
    {
        "title": "Bước 3: Điền thông tin và nhập OTP",
        "image_desc": "Form đăng ký hiện ra (các ô: Họ tên, SĐT, CMND/CCCD...). Sau đó chuyển cảnh 2 sang ô nhập mã OTP.",
        "image_file": "assets/step3.png",
        "voice": "Quý khách điền đầy đủ thông tin cá nhân, sau đó bấm Đăng ký. Hệ thống sẽ gửi mã xác thực đến số điện thoại. Quý khách nhập mã đó và bấm Tiếp tục để đăng nhập vào hệ thống.",
        "screen_text": "Form điền thông tin -> Ô nhập mã OTP",
        "actions": [
            "Nhập thông tin vào các ô trống.",
            "Bấm nút 'Đăng ký'.",
            "Chờ hiện ô OTP → Nhập 6 số.",
            "Bấm nút 'Tiếp tục'."
        ]
    },
    {
        "title": "Bước 4: Chọn sản phẩm dịch vụ",
        "image_desc": "Sau khi đăng nhập, màn hình hiện danh sách các loại thẻ/dịch vụ để chọn.",
        "image_file": "assets/step4.png",
        "voice": "Sau khi đăng nhập thành công, Quý khách thực hiện chọn loại sản phẩm dịch vụ mà mình có nhu cầu đăng ký.",
        "screen_text": "Danh sách Thẻ / Sản phẩm dịch vụ",
        "actions": ["Con trỏ di chuyển qua từng sản phẩm, sau đó click chọn 1 ô/1 dòng sản phẩm cụ thể (ví dụ: 'Thẻ tín dụng') và ô đó sẽ chuyển màu xanh."]
    },
    {
        "title": "Bước 5: Chọn tư vấn và điền thông tin (Nếu chưa có)",
        "image_desc": "Giao diện bước 5 hiển thị các tùy chọn (Hình thức tư vấn, Địa điểm, Thời gian). Bên dưới là form thông tin để điền bổ sung.",
        "image_file": "assets/step5.png",
        "voice": "Quý khách chọn hình thức tư vấn mong muốn, địa điểm và thời gian nhận tư vấn. Lưu ý: Nếu Quý khách chưa có thông tin trên hệ thống Vietcombank, hãy điền đầy đủ thông tin tại bước này.",
        "screen_text": "Dropdown lựa chọn hình thức tư vấn và địa điểm",
        "actions": [
            "Mở dropdown chọn 'Tư vấn qua điện thoại'.",
            "Mở dropdown chọn Chi nhánh.",
            "Chọn khung giờ.",
            "Kéo xuống form dưới (nếu có) → nhập bổ sung thông tin (VD: Địa chỉ, nghề nghiệp...)."
        ]
    },
    {
        "title": "Bước 6: Kiểm tra và xác nhận",
        "image_desc": "Màn hình chuyển sang bảng tổng hợp tất cả thông tin (Từ bước 3 + bước 5).",
        "image_file": "assets/step6.png",
        "voice": "Hệ thống hiển thị lại toàn bộ thông tin đã đăng ký. Quý khách vui lòng kiểm tra thật kỹ. Nếu đúng, bấm Xác nhận để tiếp tục.",
        "screen_text": "BẢNG TỔNG HỢP THÔNG TIN ĐĂNG KÝ",
        "actions": [
            "Cuộn chậm từ trên xuống để xem hết các thông tin.",
            "Bấm nút 'Xác nhận' (hoặc 'Tiếp tục')."
        ]
    },
    {
        "title": "Bước 7: Thông báo thành công và upload hồ sơ",
        "image_desc": "Cảnh 7a: Thông báo xanh 'Đăng ký SPDV thành công' hiện lên. Cảnh 7b: Popup hoặc dòng chữ yêu cầu 'Upload hồ sơ đăng ký' hiện ra và có nút 'Đồng ý'.",
        "image_file": "assets/step7.png",
        "voice": "Thông báo đăng ký thành công hiện lên. Ngay sau đó, hệ thống sẽ yêu cầu upload hồ sơ. Quý khách nhấn Đồng ý để thực hiện tải hồ sơ lên nhé!",
        "screen_text": "ĐĂNG KÝ SPDV THÀNH CÔNG! / UPLOAD HỒ SƠ",
        "actions": [
            "Popup/Thông báo hiện ra.",
            "Click vào nút 'Đồng ý'.",
            "Màn hình chọn file hiện ra → chọn file (VD: ảnh chụp CMND) → bấm Upload."
        ]
    },
    {
        "title": "KẾT THÚC",
        "image_desc": "Quay lại nhân viên, cười và kết thúc.",
        "image_file": "assets/outro.png",
        "voice": "Vậy là Quý khách đã hoàn tất đăng ký. Nhân viên Vietcombank sẽ liên hệ lại đúng giờ hẹn. Cảm ơn Quý khách!",
        "screen_text": "CẢM ƠN QUÝ KHÁCH!\nHotline hỗ trợ: 1900...",
        "actions": []
    }
]

# Quản lý trạng thái bước (Step Index) bằng Session State
if "step_index" not in st.session_state:
    st.session_state.step_index = 0

# Thanh Sidebar để điều hướng nhanh các bước
st.sidebar.header("Danh sách các cảnh")
step_options = [f"{i}: {data['title']}" for i, data in enumerate(script_data)]
selected_step = st.sidebar.radio("Đi đến cảnh:", step_options, index=st.session_state.step_index)
st.session_state.step_index = int(selected_step.split(":")[0])

# Lấy dữ liệu cảnh hiện tại
current_step = script_data[st.session_state.step_index]

# Bố cục giao diện hiển thị kịch bản
st.markdown(f'<div class="step-title">{current_step["title"]}</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("### 🖼️ Hình ảnh hiển thị (Mô phỏng)")
    # Kiểm tra xem file hình ảnh có tồn tại thực tế hay không
    if os.path.exists(current_step["image_file"]):
        st.image(current_step["image_file"], caption=current_step["image_desc"], use_container_width=True)
    else:
        # Nếu chưa có ảnh, hiển thị khung tạm thời mô tả hình ảnh
        st.info(f"💡 *[Khung hiển thị hình ảnh mẫu]*\n\n**Mô tả cảnh:** {current_step['image_desc']}")
    
    if current_step["screen_text"]:
        st.info(f"🔤 **Chữ xuất hiện trên màn hình:**\n\n `{current_step['screen_text']}`")

with col2:
    st.markdown("### 🎙️ Lời thoại / Voice-over")
    st.markdown(f'<div class="section-box voice-over">"{current_step["voice"]}"</div>', unsafe_allow_html=True)
    
    # Giả lập phát file âm thanh (nếu có file mp3 tương ứng)
    audio_file = current_step["image_file"].replace(".png", ".mp3")
    if os.path.exists(audio_file):
        st.audio(audio_file)

    if current_step["actions"]:
        st.markdown("### 🖱️ Hành động tương tác trong cảnh")
        action_html = "<div class='section-box'>"
        for i, act in enumerate(current_step["actions"], 1):
            action_html += f"<p class='action-text'>{i}. {act}</p>"
        action_html += "</div>"
        st.markdown(action_html, unsafe_allow_html=True)

# Thanh điều hướng Bottom Navigation
st.markdown("---")
btn_col1, btn_col2, btn_col3 = st.columns([1, 4, 1])

with btn_col1:
    if st.button("⬅️ Cảnh trước", disabled=(st.session_state.step_index == 0)):
        st.session_state.step_index -= 1
        st.rerun()

with btn_col2:
    # Hiển thị tiến trình dạng phần trăm
    progress_val = (st.session_state.step_index + 1) / len(script_data)
    st.progress(progress_val, text=f"Tiến độ kịch bản: {st.session_state.step_index + 1} / {len(script_data)}")

with btn_col3:
    if st.button("Cảnh sau ➡️", disabled=(st.session_state.step_index == len(script_data) - 1)):
        st.session_state.step_index += 1
        st.rerun()
