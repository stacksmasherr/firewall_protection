import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess

class FirewallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UFW Firewall Control")
        self.root.configure(bg='black')

        # Style configurations
        label_style = {'bg': 'black', 'fg': 'red', 'font': ('Helvetica', 16, 'bold')}
        button_style = {
            'bg': 'red',
            'fg': 'white',
            'activebackground': 'darkred',
            'activeforeground': 'black',
            'font': ('Helvetica', 12, 'bold'),
            'relief': 'raised',
            'bd': 5,
            'width': 20
        }

        # Create and display the label
        self.title_label = tk.Label(root, text="Manish's Firewall Protection", **label_style)
        self.title_label.pack(pady=20)

        # Create buttons with updated styles
        self.enable_button = tk.Button(root, text="Enable Firewall", command=self.enable_firewall, **button_style)
        self.disable_button = tk.Button(root, text="Disable Firewall", command=self.disable_firewall, **button_style)
        self.status_button = tk.Button(root, text="Check Firewall Status", command=self.check_status, **button_style)
        self.add_rule_button = tk.Button(root, text="Add Rule", command=self.add_rule, **button_style)
        self.block_rule_button = tk.Button(root, text="Block Rule", command=self.block_rule, **button_style)
        self.show_rules_button = tk.Button(root, text="Show Rules", command=self.show_rules, **button_style)

        # Create menu bar
        self.menu_bar = tk.Menu(root, bg='black', fg='red')
        self.root.config(menu=self.menu_bar)

        # Create File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg='black', fg='red')
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Add Rule", command=self.add_rule)
        self.file_menu.add_command(label="Block Rule", command=self.block_rule)
        self.file_menu.add_command(label="Show Rules", command=self.show_rules)

        # Place buttons on the window
        self.enable_button.pack(pady=10)
        self.disable_button.pack(pady=10)
        self.status_button.pack(pady=10)
        self.add_rule_button.pack(pady=10)
        self.block_rule_button.pack(pady=10)
        self.show_rules_button.pack(pady=10)

    def enable_firewall(self):
        self.run_ufw_command("enable", "Firewall enabled")

    def disable_firewall(self):
        self.run_ufw_command("disable", "Firewall disabled")

    def check_status(self):
        status = self.run_ufw_command("status")
        messagebox.showinfo("Firewall Status", status)

    def add_rule(self):
        port = simpledialog.askinteger("Add Rule", "Enter port number:")
        if port:
            self.run_ufw_command(f"allow {port}", f"Rule added: allow {port}")

    def block_rule(self):
        port = simpledialog.askinteger("Block Rule", "Enter port number:")
        if port: 
            self.run_ufw_command(f"deny {port}", f"Rule added: deny {port}")

    def show_rules(self):
        rules = self.run_ufw_command("status verbose")
        messagebox.showinfo("UFW Rules", rules)

    def run_ufw_command(self, command, success_message=None):
        try:
            print(command)
            result = subprocess.run(["sudo", "ufw"] + command.split(), capture_output=True, text=True, check=True)
            if success_message:
                messagebox.showinfo("Success", success_message)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error executing UFW command: {e}")
            return e.stderr.strip()

if __name__ == "__main__":
    root = tk.Tk()
    app = FirewallApp(root)
    root.mainloop()
 