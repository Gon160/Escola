package projeto;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Color;
import javax.swing.JPasswordField;

public class Registo extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JTextField txtRN;
	private JPasswordField passwordRS;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Registo frame = new Registo();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Registo() {
		setTitle("Registo");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 319, 154);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(240, 240, 240));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Nome:");
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 20));
		lblNewLabel.setBounds(10, 11, 77, 23);
		contentPane.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("Senha:");
		lblNewLabel_1.setFont(new Font("Tahoma", Font.PLAIN, 20));
		lblNewLabel_1.setBounds(10, 45, 77, 23);
		contentPane.add(lblNewLabel_1);
		
		txtRN = new JTextField();
		txtRN.setBounds(97, 16, 159, 20);
		contentPane.add(txtRN);
		txtRN.setColumns(10);
		
		passwordRS = new JPasswordField();
		passwordRS.setBounds(97, 50, 159, 20);
		contentPane.add(passwordRS);
		
		JButton btnRegistar = new JButton("Registar");
		btnRegistar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				if(!(txtRN.getText().isEmpty() && passwordRS.getText().isEmpty())) {
					Login loginframe = new Login();
					loginframe.setVisible(true);
					loginframe.setRegist(txtRN.getText(), passwordRS.getText()); 
					dispose();
				}
				
			} 
		});
		btnRegistar.setFont(new Font("Tahoma", Font.PLAIN, 20));
		btnRegistar.setBounds(69, 79, 159, 28);
		contentPane.add(btnRegistar);
		
		
	}
	
	
}
