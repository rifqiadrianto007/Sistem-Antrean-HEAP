import tkinter as tk
from tkinter import messagebox

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0

    def add_order(self, priority, order_details):
        self.queue.append((priority, self.counter, order_details))
        self.counter += 1
        self.queue.sort(key=lambda x: x[0], reverse=True)
        self.print_queue()

    def pop_order(self):
        if self.queue:
            priority, _, order_details = self.queue.pop(0)
            self.print_queue()
            return priority, order_details
        return None, None

    def is_empty(self):
        return len(self.queue) == 0

    def print_queue(self):
        heap_repr = [f"ID {order['order_id']} (Prioritas: {priority})" for priority, _, order in self.queue]
        print(f"Antrean (Array Heap): {heap_repr}")


def calculate_priority(order_type, membership, order_size):
    priority = 0
    priority += order_type * 10
    priority += membership * 5
    priority += order_size
    return priority


class PriorityQueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Antrean Cafe")
        self.root.geometry("400x400")
        self.queue = PriorityQueue()

        # Frame untuk input data
        input_frame = tk.LabelFrame(root, text="Input Data", padx=10, pady=10)
        input_frame.pack(pady=10, fill="x")

        # Input fields
        tk.Label(input_frame, text="Order ID:").grid(row=0, column=0, sticky="w")
        self.order_id_entry = tk.Entry(input_frame)
        self.order_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Order Type (1=Delivery, 2=Take-away, 3=Dine-In):").grid(row=1, column=0, sticky="w")
        self.order_type_entry = tk.Entry(input_frame)
        self.order_type_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Membership (1=Reguler, 2=VIP):").grid(row=2, column=0, sticky="w")
        self.membership_entry = tk.Entry(input_frame)
        self.membership_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Order Size (1=Large, 2=Medium, 3=Small):").grid(row=3, column=0, sticky="w")
        self.order_size_entry = tk.Entry(input_frame)
        self.order_size_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)
        
        tk.Button(button_frame, text="Tambahkan Pesanan", bg="#4caf50",command=self.add_order, width=20).pack(pady=5)
        tk.Button(button_frame, text="Proses Pesanan", bg="#2196f3", command=self.process_order, width=20).pack(pady=5)

        # Output frame
        self.output_text = tk.Text(root, height=10, width=50, state="disabled")
        self.output_text.pack(pady=10)
        self.output_text.config(borderwidth=2, relief="solid")

    def add_order(self):
        try:
            order_id = int(self.order_id_entry.get())
            order_type = int(self.order_type_entry.get())
            membership = int(self.membership_entry.get())
            order_size = int(self.order_size_entry.get())

            if order_type not in [1, 2, 3]:
                raise ValueError("Order type harus bernilai 1, 2, atau 3.")
            if membership not in [1, 2]:
                raise ValueError("Membership harus bernilai 1 atau 2.")
            if order_size not in [1, 2, 3]:
                raise ValueError("Order size harus bernilai 1, 2, atau 3.")

            priority = calculate_priority(order_type, membership, order_size)
            order_details = {
                "order_id": order_id,
                "order_type": order_type,
                "membership": membership,
                "order_size": order_size
            }
            self.queue.add_order(priority, order_details)
            messagebox.showinfo("Info", f"Pesanan ID {order_id} ditambahkan dengan prioritas {priority}.")
            self.update_output()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def process_order(self):
        if not self.queue.is_empty():
            priority, next_order = self.queue.pop_order()
            messagebox.showinfo("Pesanan Diproses", f"Pesanan ID {next_order['order_id']} diproses (Prioritas: {priority}).")
            self.update_output()
        else:
            messagebox.showinfo("Info", "Tidak ada pesanan dalam antrean.")

    def update_output(self):
        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Antrean:\n")

        for priority, _, order in self.queue.queue:
            self.output_text.insert(tk.END, f"ID {order['order_id']} (Prioritas: {priority})\n")
        self.output_text.config(state="disabled")


# Penggunaan class PriorityQueueApp untuk aplikasi tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = PriorityQueueApp(root)
    root.mainloop()
