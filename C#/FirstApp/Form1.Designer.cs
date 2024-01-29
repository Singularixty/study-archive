namespace FirstApp
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Title = new System.Windows.Forms.Label();
            this.TextInput = new System.Windows.Forms.TextBox();
            this.UnitSelector = new System.Windows.Forms.ComboBox();
            this.button1 = new System.Windows.Forms.Button();
            this.Output = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // Title
            // 
            this.Title.AutoSize = true;
            this.Title.Font = new System.Drawing.Font("Microsoft JhengHei", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Title.ForeColor = System.Drawing.Color.White;
            this.Title.Location = new System.Drawing.Point(12, 9);
            this.Title.Name = "Title";
            this.Title.Size = new System.Drawing.Size(250, 26);
            this.Title.TabIndex = 0;
            this.Title.Text = "Temperature Convertor";
            this.Title.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // TextInput
            // 
            this.TextInput.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.TextInput.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.TextInput.Font = new System.Drawing.Font("Microsoft YaHei UI", 20.75F);
            this.TextInput.ForeColor = System.Drawing.SystemColors.Window;
            this.TextInput.Location = new System.Drawing.Point(17, 45);
            this.TextInput.Name = "TextInput";
            this.TextInput.Size = new System.Drawing.Size(268, 36);
            this.TextInput.TabIndex = 1;
            this.TextInput.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.TextInput.TextChanged += new System.EventHandler(this.TextInput_TextChanged);
            // 
            // UnitSelector
            // 
            this.UnitSelector.BackColor = System.Drawing.SystemColors.ControlLightLight;
            this.UnitSelector.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.UnitSelector.FlatStyle = System.Windows.Forms.FlatStyle.System;
            this.UnitSelector.Font = new System.Drawing.Font("Microsoft YaHei UI", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.UnitSelector.FormattingEnabled = true;
            this.UnitSelector.Items.AddRange(new object[] {
            "C",
            "F"});
            this.UnitSelector.Location = new System.Drawing.Point(291, 45);
            this.UnitSelector.Name = "UnitSelector";
            this.UnitSelector.Size = new System.Drawing.Size(121, 36);
            this.UnitSelector.TabIndex = 2;
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.button1.Cursor = System.Windows.Forms.Cursors.Hand;
            this.button1.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.button1.FlatAppearance.BorderSize = 0;
            this.button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button1.Font = new System.Drawing.Font("Microsoft YaHei UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.Location = new System.Drawing.Point(17, 87);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(395, 37);
            this.button1.TabIndex = 3;
            this.button1.Text = "Convert";
            this.button1.UseVisualStyleBackColor = false;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Output
            // 
            this.Output.AutoSize = true;
            this.Output.Font = new System.Drawing.Font("Microsoft JhengHei", 7.75F, System.Drawing.FontStyle.Bold);
            this.Output.ForeColor = System.Drawing.Color.White;
            this.Output.Location = new System.Drawing.Point(19, 132);
            this.Output.Name = "Output";
            this.Output.Size = new System.Drawing.Size(16, 15);
            this.Output.TabIndex = 4;
            this.Output.Text = "...";
            this.Output.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(32)))), ((int)(((byte)(32)))), ((int)(((byte)(32)))));
            this.ClientSize = new System.Drawing.Size(428, 157);
            this.Controls.Add(this.Output);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.UnitSelector);
            this.Controls.Add(this.TextInput);
            this.Controls.Add(this.Title);
            this.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.Name = "Form1";
            this.Text = "Temperature Convertor";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Title;
        private System.Windows.Forms.TextBox TextInput;
        private System.Windows.Forms.ComboBox UnitSelector;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label Output;
    }
}

