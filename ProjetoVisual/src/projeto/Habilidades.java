package projeto;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import projeto.champions.Champions;

import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JLabel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JScrollPane;
import javax.swing.ScrollPaneConstants;
import javax.swing.JTextField;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.Font;

public class Habilidades extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private Champions ch;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Habilidades frame = new Habilidades();
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
	public Habilidades() {
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 314);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JScrollPane scrollPaneHabilidade = new JScrollPane();
		scrollPaneHabilidade.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
		scrollPaneHabilidade.setBounds(10, 58, 414, 206);
		contentPane.add(scrollPaneHabilidade);
		
		JTextArea txtHabilidade = new JTextArea();
		scrollPaneHabilidade.setViewportView(txtHabilidade);
		txtHabilidade.setLineWrap(true);
		txtHabilidade.setWrapStyleWord(true);
		
		JComboBox comboBox = new JComboBox();
		comboBox.setFont(new Font("Tahoma", Font.PLAIN, 20));
		comboBox.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
					if(comboBox.getSelectedItem() == "Passiva"){
						txtHabilidade.setText(ch.getP());
					} else if (comboBox.getSelectedItem() == "Q") {
						txtHabilidade.setText(ch.getQ());
					} else if (comboBox.getSelectedItem() == "W") {
						txtHabilidade.setText(ch.getW());
					}else if (comboBox.getSelectedItem() == "E") {
						txtHabilidade.setText(ch.getE());
					}else if (comboBox.getSelectedItem() == "R") {
						txtHabilidade.setText(ch.getR());
					}
			}
		});
		comboBox.setModel(new DefaultComboBoxModel(new String[] {"Escolha a habilidade", "Passiva", "Q", "W", "E", "R"}));
		comboBox.setBounds(10, 11, 199, 31);
		contentPane.add(comboBox);
		
		JButton btnNewButton = new JButton("Voltar");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				HL HLframe = new HL();
				HLframe.Ch(ch);
				HLframe.setTitle(ch.getNome());
				HLframe.setVisible(true);
				
				
				dispose();
			}
		});
		btnNewButton.setFont(new Font("Tahoma", Font.BOLD, 20));
		btnNewButton.setBounds(225, 11, 199, 31);
		contentPane.add(btnNewButton);
	}
	
	public void Ch(Champions ch) {
		this.ch = ch;
	}
	
}
