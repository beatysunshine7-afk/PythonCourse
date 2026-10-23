import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit,
    QPushButton, QGridLayout, QMessageBox
)


class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("May tinh bo tui")
        self.setFixedSize(320, 380)

        self.o_hien_thi = QLineEdit()
        self.o_hien_thi.setReadOnly(True)
        self.o_hien_thi.setAlignment(Qt.AlignRight)
        self.o_hien_thi.setMinimumHeight(45)
        self.o_hien_thi.setStyleSheet("font-size: 24px;")

        layout = QGridLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        layout.addWidget(self.o_hien_thi, 0, 0, 1, 4)

        cac_nut = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"]
        ]

        for hang, danh_sach_nut in enumerate(cac_nut, start=1):
            for cot, ky_tu in enumerate(danh_sach_nut):
                nut = QPushButton(ky_tu)
                nut.setMinimumHeight(50)
                nut.setStyleSheet("font-size: 20px;")

                if ky_tu == "C":
                    nut.clicked.connect(self.xoa)
                else:
                    nut.clicked.connect(
                        lambda checked, k=ky_tu: self.bam_nut(k)
                    )

                layout.addWidget(nut, hang, cot)

        nut_bang = QPushButton("=")
        nut_bang.setMinimumHeight(50)
        nut_bang.setStyleSheet("font-size: 20px;")
        nut_bang.clicked.connect(self.tinh_ket_qua)

        layout.addWidget(nut_bang, 5, 0, 1, 4)

        self.setLayout(layout)

    def bam_nut(self, ky_tu):
        bieu_thuc = self.o_hien_thi.text()
        self.o_hien_thi.setText(bieu_thuc + ky_tu)

    def xoa(self):
        self.o_hien_thi.clear()

    def tinh_ket_qua(self):
        bieu_thuc = self.o_hien_thi.text()

        if not bieu_thuc:
            QMessageBox.critical(
                self, "Loi", "Vui long nhap phep tinh."
            )
            return

        try:
            if any(
                ky_tu not in "0123456789.+-*/"
                for ky_tu in bieu_thuc
            ):
                raise ValueError

            ket_qua = eval(
                bieu_thuc, {"__builtins__": {}}, {}
            )
            self.o_hien_thi.setText(str(ket_qua))

        except ZeroDivisionError:
            QMessageBox.critical(
                self, "Loi", "Khong the chia cho 0."
            )

        except (SyntaxError, TypeError, ValueError, OverflowError):
            QMessageBox.critical(
                self, "Loi", "Phep tinh khong hop le."
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())