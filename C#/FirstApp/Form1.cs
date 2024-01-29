using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace FirstApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (UnitSelector.SelectedItem != null)
            {
                string SelectedUnit = UnitSelector.SelectedItem.ToString();
                string TempValue = TextInput.Text;

                if (SelectedUnit.Equals("C", StringComparison.OrdinalIgnoreCase))
                {
                    double fahrenheitValue = (Convert.ToDouble(TempValue) * 9 / 5) + 32;
                    Output.Text = fahrenheitValue.ToString("F2") + "F";
                }
                else if (SelectedUnit.Equals("F", StringComparison.OrdinalIgnoreCase))
                {
                    double celsiusValue = (Convert.ToDouble(TempValue) - 32) * 5 / 9;
                    Output.Text = celsiusValue.ToString("F2") + "C";
                }
                else
                {
                    MessageBox.Show("Invaild Unit!, Please specify a temperature unit (C/F)", "Error!");
                }
            }
            else
            {
                MessageBox.Show("Please specify a temperature unit", "Error!");
            }
        }

        private void TextInput_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
