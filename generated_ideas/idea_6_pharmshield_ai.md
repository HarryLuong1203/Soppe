# BÁO CÁO THẨM ĐỊNH Ý TƯỞNG: PharmShield AI: Autonomous Prescription Verification & Counterfeit Drug Detection Agent for Online Pharmacies

## 1. Chi tiết diễn biến từng vòng

### Vòng 1: Khởi tạo & Kiểm tra Độc quyền
- **Agent 1 (Ideator):** Đề xuất ý tưởng *PharmShield AI: Autonomous Prescription Verification & Counterfeit Drug Detection Agent for Online Pharmacies* thuộc nhóm *Deep Domain AI*. Vấn đề cốt lõi: Nhu cầu mua thuốc online trên Shopee Health tăng mạnh nhưng đối mặt nguy cơ đơn thuốc kê đơn (Rx) bị làm giả bằng photoshop và nguy cơ tương tác thuốc nguy hiểm, đe dọa sức khỏe người tiêu dùng và rủi ro pháp lý cho sàn TMĐT.
- **Agent 2 (Novelty Checker):** Kết luận **HỢP LỆ (PASS)**. Khác biệt với app tra cứu thuốc thông thường: Đây là Agent thẩm định y khoa chuyên sâu (Clinical Forensics) kết hợp công nghệ phát hiện ảnh giả mạo con dấu/chữ ký và tra cứu chéo Dược thư Quốc gia theo thời gian thực.

### Vòng 2: Chấm điểm Rubric Vô danh (Agent 3 - Stateless)
- **Gate (Build Direction):** PASS
- **Tiêu chí 2 (Gần gũi & Thiết thực - 30%):** 8.9 / 10
- **Tiêu chí 3 (Giá trị mang lại - 30%):** 9.3 / 10
- **Tiêu chí 4 (Khả thi 7h Codex - 40%):** 8.3 / 10
- **Điểm tổng kết:** **8.78 / 10** $\rightarrow$ **ĐẠT** (Vượt ngưỡng 8.0/10).
- **Điểm yếu nhất:** Khả thi build 7h Codex (8.3/10) — *Cần nạp sẵn cơ sở dữ liệu mẫu gồm 50 loại thuốc phổ biến và 10 cặp tương tác thuốc nguy hiểm để API tra cứu tức thời.*

### Vòng 3: Tinh chỉnh Cấu trúc & Tự phản chiếu (Agent 4, 5, 6)
- **Agent 4:** Chuẩn hóa giao diện thành kiến trúc *Unified Split-Screen Operations Cockpit* (Single 16:9 Dashboard) để Codex build trong 3.5h, loại bỏ nguy cơ phân tán UI.
- **Agent 5:** Duyệt giải pháp theo Checklist Mục 6, yêu cầu tích hợp chế độ 1-Click Auto-Pilot Demo.
- **Agent 6:** Tổng hợp hồ sơ dự thi hoàn chỉnh, xác nhận độ trôi dạt độc quyền là 0% (100% Safe).

---

## 2. HỒ SƠ Ý TƯỞNG

* **Tên sản phẩm**: **PharmShield AI: Autonomous Prescription Verification & Counterfeit Drug Detection Agent for Online Pharmacies**  
  *Slogan*: *"Guarding Public Health in SEA — Autonomous Rx Authenticity Verification & Drug Interaction Sentinel in 4 Seconds."*
* **Build Direction**: **Deep Domain AI (Primary) + Autonomous & Adaptive AI (Digital Healthcare & Compliance)**
* **Bối cảnh (thực trạng hiện nay)**:  
  Ngành hàng Dược phẩm và Thực phẩm chăm sóc sức khỏe trên Shopee (Shopee Health, Bách Hóa Online) đang tăng trưởng vượt bậc tại Đông Nam Á. Tuy nhiên, việc kinh doanh thuốc kê đơn (Prescription-only Medication - Rx) qua mạng chịu sự thanh kiểm tra cực kỳ gắt gao của Bộ Y tế các nước (Việt Nam, Indonesia, Singapore).
* **Hậu quả**:  
  1. **Hiểm họa đe dọa tính mạng người tiêu dùng do đơn thuốc giả mạo (Counterfeit Rx & Drug Abuse)**: Tình trạng người mua sử dụng các đơn thuốc cũ tải trên mạng, dùng phần mềm Photoshop chỉnh sửa ngày tháng hoặc tên thuốc an thần, kháng sinh liều cao diễn ra phức tạp. Uống sai thuốc hoặc sử dụng các loại thuốc xung khắc có thể dẫn tới sốc phản vệ, suy gan thận cấp hoặc tử vong.
2. **Rủi ro đình chỉ hoạt động và chế tài pháp lý tiền tỷ cho sàn TMĐT**: Các nhà thuốc đối tác trên Shopee Mall không có đủ dược sĩ để đọc và đối soát từng tờ đơn thuốc viết tay nguệch ngoạc của bệnh viện. Nếu để lọt việc bán thuốc cấm kê đơn trực tuyến, nhà thuốc và sàn TMĐT đối mặt nguy cơ bị cơ quan quản lý tước giấy phép kinh doanh, phạt tiền hàng tỷ đồng và hủy hoại uy tín thương hiệu.
* **Giải pháp và Kiến trúc giải pháp**:  
  **Cơ chế giải pháp cốt lõi**:
PharmShield AI là **Agent thẩm định y khoa & an toàn dược phẩm tự chủ chuyên sâu (Autonomous Clinical Forensics & Pharmacology Agent)**:
- **Giám định pháp y đơn thuốc kỹ thuật số (Multimodal Rx Forensics)**: Sử dụng GPT-4o Vision phân tích ảnh chụp đơn thuốc: Đọc chữ viết tay bác sĩ, nhận diện con dấu tròn bệnh viện, và tự động soi chiếu các dị thường chỉnh sửa ảnh (tẩy xóa chữ, sai lệch phông chữ, metadata bị can thiệp bởi phần mềm chỉnh sửa).
- **Thẩm định tương tác thuốc & liều lượng tự động (Autonomous Drug-Drug Interaction - DDI)**: Tự động đối chiếu các loại thuốc trong đơn với giỏ hàng của người mua và Dược thư Quốc gia. Nếu phát hiện 2 hoạt chất có tương tác nguy hiểm (ví dụ thuốc hạ huyết áp dùng chung thuốc chống viêm NSAID) hoặc liều dùng vượt trần an toàn theo độ tuổi, Agent lập tức phát cảnh báo đỏ và ngăn chặn thanh toán.
- **Cấp mã xác thực đơn thuốc điện tử (1-Click Digital Rx Clearance)**: Tự động trích xuất thông tin bác sĩ, số chứng chỉ hành nghề, chẩn đoán bệnh và lập bộ hồ sơ thẩm định y khoa chuẩn mẫu gửi cho Dược sĩ phụ trách chỉ trong 4 giây.

**Kiến trúc giải pháp (Unified Split-Screen Operations Cockpit)**:
- **Panel 1 (Patient Rx Upload & Cart Ingestion)**: Kéo thả ảnh đơn thuốc bệnh viện và hiển thị giỏ hàng Shopee Health.
- **Panel 2 (Clinical OCR & Forensic Tamper Radar)**: Bóc tách tên hoạt chất viết tay và bản đồ nhiệt phát hiện chỉnh sửa ảnh giả mạo.
- **Panel 3 (Autonomous Pharmacology & Safety Engine)**: Ma trận kiểm tra tương tác thuốc, cảnh báo chống chỉ định và liều dùng.
- **Panel 4 (Rx Clearance & Pharmacist Decision Console)**: Trạng thái phê duyệt đơn thuốc điện tử và nút 1-click chuyển đơn sang khâu đóng gói.
* **Kịch bản Demo (rõ ràng)**:  
  **Kịch bản Demo 3 phút chuẩn chỉnh cho Ban Giám Khảo (180 giây)**:
- **00:00 - 00:45 (Hook & Problem)**: Trình bày một đơn thuốc viết tay bị người mua dùng Photoshop sửa ngày khám từ năm 2024 thành tháng 10/2026 để cố tình mua thuốc ngủ liều cao trên Shopee Mall.
- **00:45 - 01:30 (Action 1: Bắt quả tang đơn thuốc giả mạo trong 3 giây)**: Đưa ảnh đơn thuốc vào Panel 1. Panel 2 lập tức khoanh vùng đỏ vị trí ngày tháng: *Phát hiện can thiệp phông chữ kỹ thuật số (Font Inconsistency, Confidence 98.6%) -> Đơn thuốc bị làm giả*. Hệ thống phát lệnh từ chối ngay lập tức.
- **01:30 - 02:15 (Action 2: Ngăn chặn tương tác thuốc chết người)**: Tải lên một đơn thuốc thật hợp lệ của bệnh viện, nhưng giỏ hàng của khách lại tự ý thêm thuốc giảm đau liều cao. Panel 3 lập tức lóe cảnh báo `[CRITICAL DDI WARNING: Tương tác nguy cơ xuất huyết dạ dày cấp]`. Agent tự động loại sản phẩm xung khắc ra khỏi giỏ hàng và tư vấn thuốc an toàn thay thế.
- **02:15 - 03:00 (Giá trị pháp lý & Vận hành)**: Panel 4 cấp mã *Rx Verified Token* cho đơn hàng hợp lệ, thời gian phê duyệt thuốc từ 20 phút giảm xuống 4 giây. Dược sĩ chỉ cần bấm duyệt 1 chạm, đảm bảo an toàn tuyệt đối cho Shopee Health.

---

## 3. Trạng thái hệ thống cập nhật

```json
{
    "idea_id": 6,
    "title": "PharmShield AI: Autonomous Prescription Verification & Counterfeit Drug Detection Agent for Online Pharmacies",
    "build_direction": "Deep Domain AI (Primary) + Autonomous & Adaptive AI (Digital Healthcare & Compliance)",
    "final_score": 8.78,
    "verdict": "ĐẠT",
    "status": "APPROVED_FOR_HACKATHON",
    "generated_file": "generated_ideas/idea_6_pharmshield_ai.md"
}
```
